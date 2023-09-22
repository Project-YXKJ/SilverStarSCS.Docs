.. _service_counter: 

===============
Service counter
===============

Using service counter allows users to remind regular mechanical maintenance.

**Here is a formula**:

.. math::
   :name: Service Remaining Amount

   N_{\text{Remaining amount}} = A61_{\text{reset value of the service counter}} - 
   A63_{\text{service counter value}}

**Setup steps**:

1. Set an appropriate value for `A 62`_, every time N stitches are sewn which
   set by this parameter, the counter value `A 63`_ increases by 1.
2. Set an appropriate value for `A 61`_, this is a very variable value, which 
   depends on how often you want to maintain.
3. Set `A 60`_ to 1, enable the counter.
4. Refer to the beginning of this chapter `Service Remaining Amount`_, 
   as the sewing, the remaining amount is counted down, when it reaches 0, 
   the machine will stop, and the controller will throw a warning. A reset 
   is needed if you want continue.

Parameter List
==============

A 60
----

.. dropdown:: Service Stitch Counter <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Active service stitch counter:
     | 0 = Off;
     | 1 = On.

A 61
----

.. dropdown:: Service Counter Reset Value <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  Reset value of service stitch counter
   
A 62
----

.. dropdown:: Service Counter Factor <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  stitches
   -Description  Every sew over this number of stitches,increment the counter by 1

A 63
----

.. dropdown:: Service Counter Value <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  -- 
   -Description  The current value of service stitch counter
