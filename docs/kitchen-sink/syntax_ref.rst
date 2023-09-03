.. _syntax_ref:


================
Syntax Reference
================

reStructuredText
================

List Table
----------

.. list-table:: Parameter list
  :widths: 4 5 5 10 70

  * - No.
    - Max
    - Min
    - Unit
    - Description
  * - O56
    - 4095
    - 0  
    - --
    - The maximum pedal input when position 2, value > O57 

Sphinx Design
=============

Dropdown
--------

.. dropdown:: < > Detail 
   :animate: fade-in-slide-down
   
   -Max  maximum
   -Min  minimum
   -Unit  unit
   -Description
     | The description can also start on the next line.
     | value1: text;
     | value2: text.


Grid
----
.. grid:: 1 2 3 4
  :margin: 4 4 0 0
  :gutter: 1

  .. grid-item-card:: 标题1
    :link: www.baidu.com
    :link-type: url
    
    内容1
  
  .. grid-item-card:: 标题2

    内容1
