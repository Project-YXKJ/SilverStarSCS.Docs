.. _bobbin_monitor:

==============
Bobbin Counter
==============

Using Lower thread counter allows users to know the remaining thread amount.

**Here is a formula**:

.. math::
   :name: Bobbin Remaining Amount

   N_{\text{Remaining thread amount}} 
   = O43_{\text{reset value of the bobbin thread counter}} - O44_{\text{bobbin thread counter value}}

**Setup steps**:

1. Set an appropriate value for `O 19`_, every time N stitches are sewn which set by
   this parameter, the counter value `O 44`_ increases by 1.
2. Set an appropriate value for `O 43`_, this is a very variable value, which depends
   on the size of the bobbin and the thickness of the thread.
3. Choose when to throw a warning by setting `O 20`_, immediately or after thread cutting.
4. Set `A 12`_ to 1, enable the counter.
5. Refer to the beginning of this chapter `Bobbin Remaining Amount`_, as the sewing,
   the remaining amount is counted down, when it reaches 0, the machine will stop, 
   and the controller will throw a warning. A reset is needed if you want continue.

Parameter List
==============

A 12
----

.. dropdown:: Bobbin Stitch Counter <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  --
   -Description
     | Activate the Bobbin stitch counter:
     | 0 = Off;
     | 1 = On.

O 19
----

.. dropdown:: Factor of bobbin counter <...>
   :animate: fade-in-slide-down
   
   -Max  200
   -Min  1
   -Unit  stitches
   -Description  Every sew over this number of stitches,increment the counter by 1.

O 20
----

.. dropdown:: Timming of Warning(Bobbin Counter) <...>
   :animate: fade-in-slide-down
   
   -Max  1
   -Min  0
   -Unit  stitches
   -Description  
     | When to throw a warning if bobbin counter reaches 0:
     | 0 = after thread cutting;
     | 1 = immediately
     
O 43
----

.. dropdown:: Bobbin Stitch Counter Reset Value <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  1
   -Unit  --
   -Description  Bobbin supply capacity. This is a very variable value,which depends
     on the size of the bobbin and the thickness of the thread

O 44
----

.. dropdown:: Bobbin Stitch Counter Value <...>
   :animate: fade-in-slide-down
   
   -Max  9999
   -Min  0
   -Unit  --
   -Description  The current value of bobbin stitch counter, the reset value minus 
     this value is remaining value.
