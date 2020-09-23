=========================
Collapsible Investigation
=========================

This is an investigation into collapsible text boxes for sphinx.
This is regular text written in the .rst file.
Below is a collapsible box created by an extension.

Factorial Module
================

.. collapsible::
   :title: Factorial Details

   This is some regular text inside the collapsible
   Here is a rst code-block:
   
   .. code-block:: python

      print("hello world")

   Below this like is an auto-generated module

   .. automodule:: factorial
         :members:

This text is not part of the collapsible


.. collapsible::
   :title: Collapsible 2
   
   here is some stuff in the collapsible.
   
   .. code-block:: python
   
      print("collapsible 2")
      
   end
   
this is after collapsible 2