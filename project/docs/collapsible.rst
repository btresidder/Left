=========================
Collapsible Investigation
=========================

This is an investigation into collapsible text boxes for sphinx.
This is regular text written in the .rst file.
Below is an attempt at making a collapsible box.

.. raw:: html

   <details>
   <summary><b>Press this for drop down</b></summary>
   <p>This is a bunch of text I have written.</p>
   </details>

Here is some more text outside of the collapsible to see what it will do.

.. raw:: html

   <details>
   <summary>Here is a box that has some regular rst inside it</summary>

This is a standard rst sentence.

.. code-block:: python

   print("hello world")

this is outside the code block.

.. raw:: html

   </details>



this is below the collapsible.

below this is a call to the hello world extension:

.. helloworld::

this is after the extension call
