=========================
Collapsible Investigation
=========================

This is an investigation into collapsible text boxes for sphinx.
This is regular text written in the .rst file.
Below is a collapsible box created by an extension.

factorial main
==============
.. automodule:: factorial
         :members:

.. collapsible::
   :title: Factorial Module

   This is some regular text inside the collapsible

   .. code-block:: python

      print("hello world")

   Here is some more text. Below is a auto-gen module
   


This text is not part of the collapsible
