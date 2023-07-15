'''Test whether import in multiple files import multiple times
In the end, no it does not, only one import runs.
'''

import home
import home_menu

print(f"__name__ in my menu_menu file: {__name__}")