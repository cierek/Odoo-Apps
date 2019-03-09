Dear user, 
This module is initially configured to work straight away and it just needs a "website" module. However, if you are using "Email Marketing" module you need to edit the __manifest__.py as well as __openerp__.py files. There is instruction in the files and all opeartion is just about removing "#" from line 24.

The reason that the line 24 is commented is that:
- Module would not work and cause a crash if user would not have "Email Marketing" installed
- That saves your money as there is only one module to buy

I kope you will enjoy using the module.

Kind regards,
Piotr Cierkosz