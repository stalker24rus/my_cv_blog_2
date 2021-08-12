import functools
# from django.core.mail import send_mail


def exception_catcher(logger, except_return):
    """
    logger - it will be the object of logging.getLogger()
    except_return - return result that function if have exception
    """
    def decorator(view):
        @functools.wraps(view)
        def wraper(*args, **kwargs):
            try:
                return view(*args, **kwargs)
            except Exception as e:
                logger.warning(e)
                # send_mail(subject, message, 'razorstent@gmail.com', [cd['to']])
                return except_return
        return wraper
    return decorator
