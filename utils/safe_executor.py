"""
author: Maxim Van den Abeele
date: 30/03/2023
"""
import logging
import multiprocessing
import sys
import threading
from enum import Enum
from multiprocessing import Queue


class DefaultQueue(Enum):
    """Default queue items"""
    START_QUEUE = ["self", "start"]
    STOP_QUEUE = ["self", "stop"]


class SafeProcess(multiprocessing.Process):
    """A safe process which handles messages of a queue
    """
    def __init__(self, name, queue : Queue, *args, **kwargs):
        super().__init__(daemon=True, *args, **kwargs)
        self._queue = queue
        self._name = name
        self._executor = SafeExecutor()
        self._logger = logging.getLogger(f"Process {name}")
        self.cb_message = None

    def run(self):
        process = self._target(*self._args)
        self.cb_message = process.handle_message
        job_name = self._executor.submit(f"{self.name} messages", self._message_handler)
        # Put a start event in the queue
        self._queue.put([DefaultQueue.START_QUEUE, []])
        if hasattr(process, "run"):
            process.run()
            # Used to terminate the message queue
            self._queue.put([DefaultQueue.STOP_QUEUE, []])

        self._executor.wait_on_job(job_name)
        del process

    def _message_handler(self):
        while True:
            try:
                item = self._queue.get()
                self._logger.debug("Submitting %s", str(item))
                job = self._executor.submit("queue", self.cb_message, item)
                # Terminate the loop if stop command is received
                if 'stop' in item[0].value:
                    # Cleanly exit
                    self._executor.wait_on_job(job)
                    return
            except:
                self._logger.error("Error occured check logs", exc_info=1)
                raise

class SafeExecutor:
    """Safe executor prints exceptions when they occur in submitted functions
    this makes life easyer when debugging
    """
    _jobs: dict[str, threading.Thread]

    def __init__(self, max_workers: int=16):
        self._logger = logging.getLogger("Safe executor")
        #TODO: Currently not used but could be used to limit number of threads
        self._max_workers = max_workers
        self._jobs = {}

        logger = multiprocessing.log_to_stderr()
        logger.setLevel(logging.WARNING)

    def submit(self, name : str, fnc : callable, *args, **kwargs) -> str:
        """submit a function to be executed by a threadpool while mainting error messages

        Args:
            name (string): Name of the function to be exectued
            fnc (callable): Callable which is executed with *args and **kwargs
        Returns:
            (str): ID of the job which you can use to wait on it.
        """
        if name in self._jobs:
            name = f"{name}{int(name[-1])+1}"
        else:
            name = f"{name}_0"

        job = threading.Thread(target=self._submit,
                               daemon=True,
                               args = [fnc, name, *args],
                               kwargs=kwargs)
        job.start()

        self._jobs[name] = job
        return name

    def is_running(self, name : str) -> bool:
        """Find out if a job is already running or not

        Args:
            name (str): Name of the job

        Returns:
            bool: Returns True if the job is currently scheduled otherwise False
        """
        return name in self._jobs

    def wait_on_job(self, name : str):
        """Wait on a specific job to finish

        Args:
            name (str): Name given to the job

        Returns:
        """
        # Job already finished
        if not name in self._jobs:
            return None
        # Wait on job result
        return self._jobs[name].join()

    def _submit(self, fnc, name, *args, **kwargs):
        try:
            fnc(*args, **kwargs)
            if name in self._jobs:
                self._jobs.pop(name)
        except RuntimeError:
            self._logger.error("Shutting down executor and closing app")
            sys.exit()
        except Exception:
            self._logger.error("Exception occured in execution of %s", name, exc_info=1)
            raise

    def __del__(self):
        for job in self._jobs:
            self.wait_on_job(job)
