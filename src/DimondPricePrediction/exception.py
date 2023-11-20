import sys


class Customexception(Exception):
    def __init__(self, error_message ,error_details:sys):
        self.error_message = error_message
        _,_,exe_tb = error_details.exc_info()
        
        self.lineno= exe_tb.tb_lineno
        self.file_name= exe_tb.tb_frame.f_code.co_filename   
        
    def __str__(self):
        return "Error occured in python scrit name [{0}] line number [{1}] error massage [{2}]".format(
            self.file_name, self.lineno, self.error_message)
    
    
if __name__=="__main__":
    try :
            
        a=1/1
    except Exception as e:
        raise Customexception(e,sys)