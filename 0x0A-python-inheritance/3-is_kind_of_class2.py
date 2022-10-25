#!/isr/bin/python3
 def is_kind_of_class(obj, a_class):
     """Check if an object is an instamce of a specific class or built in class"""
     if isinstance(obj, a_class):
         return True
     else:
         return False
