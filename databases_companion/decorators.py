__version__='1.1.0'
__author__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2025-02-3'

import traceback, inspect
from functools import wraps
from decimal import Decimal, InvalidOperation
from envrio_logger.logger import alchemy, influxdb

class DatabaseDecorators():

    def __init__(self, SessionLocal, Session):
        self.SessionLocal = SessionLocal()
        self.Session = Session

    def session_handler_add_delete_update(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db: self.Session = kwargs.get('db') or self.SessionLocal
            try:
                result = func(*args, db=db, **kwargs)
                db.commit()
                alchemy.info(f"{func.__name__} executed successfully")
                return result
            except Exception as e:
                db.rollback()
                alchemy.error(f"Error occurred {func.__name__}: {str(e)}")
                alchemy.error(traceback.format_exc())
                return {"message": "An unexpected error occurred. Please try again later."}
            finally:
                db.close()
        return wrapper

    def session_handler_query(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            db: self.Session = kwargs.get('db') or self.SessionLocal
            try:
                result = func(*args, db=db, **kwargs)
                alchemy.info(f"{func.__name__} executed successfully")
                return result
            except Exception as e:
                alchemy.error(f"Error occurred {func.__name__}: {str(e)}")
                alchemy.error(traceback.format_exc())
                return {"message": "An unexpected error occurred. Please try again later."}
            finally:
                db.close()
        return wrapper

    @staticmethod
    def influxdb_error_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                # Try to execute the wrapped function
                return func(*args, **kwargs)
            except Exception as e:
                # Log the exception, traceback and return a structured error response
                influxdb.error(f"Error in {func.__name__}: {str(e)}")
                influxdb.error(traceback.format_exc())
                return {"message": f"Error in {func.__name__}: {str(e)}", "status": "error"}
        return wrapper

class DTypeValidator:

    @staticmethod
    def validate_int(*param_names):
        """Decorator to validate that a specific parameter is an integer."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Get the function's signature
                sig = inspect.signature(func)
                bound_args = sig.bind_partial(*args, **kwargs).arguments    

                # Check both positional (args) and keyword (kwargs) arguments
                for param_name in param_names:
                    # Check if the param is in keyword arguments
                    if param_name in bound_args:
                        if not isinstance(bound_args[param_name], int):
                            alchemy.error(f"{param_name} must be an integer")
                            return {"message": "Bad Request", "errors": [f"{param_name} must be an integer"]}
                    
                    
                # Call the original function if validation passes
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def validate_str(*param_names):
        """Decorator to validate that a specific parameter is an integer."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Get the function's signature
                sig = inspect.signature(func)
                bound_args = sig.bind_partial(*args, **kwargs).arguments    

                # Check if the parameter is present and validate its type
                for index, param_name in enumerate(param_names):
                    if bound_args.get('kwargs'):
                        if param_name in bound_args['kwargs'] and not isinstance(bound_args['kwargs'][param_name], str):
                            alchemy.error(f"{param_name} must be a string")
                            return {"message": "Bad Request", "errors": [f"{param_name} must be a string"]}
                    elif bound_args.get('args'):
                        if not isinstance(bound_args['args'][index], str):
                            alchemy.error(f"{param_name} must be a string")
                            return {"message": "Bad Request", "errors": [f"{param_name} must be a string"]}
                    
                # Call the original function if validation passes
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def validate_float(*param_names):
        """Decorator to validate that a specific parameter is an integer."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Get the function's signature
                sig = inspect.signature(func)
                bound_args = sig.bind_partial(*args, **kwargs).arguments    

                # Check if the parameter is present and validate its type
                for index, param_name in enumerate(param_names):
                    if bound_args.get('kwargs'):
                        if param_name in bound_args['kwargs'] and not isinstance(bound_args['kwargs'][param_name], float):
                            return {"message": "Bad Request", "errors": [f"{param_name} must be float"]}
                    elif bound_args.get('args'):
                        if not isinstance(bound_args['args'][index], float):
                            return {"message": "Bad Request", "errors": [f"{param_name} must be float"]}
                    
                # Call the original function if validation passes
                return func(*args, **kwargs)
            return wrapper
        return decorator

    @staticmethod
    def validate_decimal(*param_names):
        """Decorator to validate that a specific parameter is a DECIMAL(10,6)."""
        def decorator(func):
            def wrapper(*args, **kwargs):
                # Get the function's signature
                sig = inspect.signature(func)
                bound_args = sig.bind_partial(*args, **kwargs).arguments    

                # Ensure kwargs exists and is a dictionary
                if "kwargs" in bound_args and isinstance(bound_args["kwargs"], dict):
                    for param_name in param_names:
                        if param_name in bound_args["kwargs"]:
                            value = bound_args["kwargs"][param_name]

                            try:
                                # Convert to Decimal and enforce 6 decimal places
                                bound_args["kwargs"][param_name] = Decimal(value).quantize(Decimal('0.000001'))
                            except (ValueError, InvalidOperation):
                                # Return an error if conversion fails
                                return {"message": "Bad Request", "errors": [f"{param_name} must be a decimal with up to 6 decimal places"]}

                # Call the original function with modified arguments
                return func(*args, **bound_args["kwargs"])

            return wrapper
        return decorator