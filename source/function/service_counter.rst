Service counter
===============

Using service counter allows users to remind regular mechanical maintenance.

Quick start
-----------

Following steps:

1. Set an appropriate value for :option:`A62`, every time N stitches are sewn which set
   by this parameter, the counter value :option:`A63` increases by 1.
2. Set an appropriate value for :option:`A61`, this is a very variable value, which
   depends on how often you want to maintain.
3. Set :option:`A60` to 1, enable the counter.
4. Refer to the beginning of this chapter `Service Remaining Amount`_, as the sewing,
   the remaining amount is counted down, when it reaches 0, the machine will stop, and
   the controller will throw a warning. A reset is needed if you want continue.

How it works?
~~~~~~~~~~~~~

.. math::
    :name: Service Remaining Amount

    N_{\text{Remaining amount}} = A61_{\text{reset value of the service counter}} -
    A63_{\text{service counter value}}

Quick reference
---------------

This table summarizes which parameter should be used for service counter:

=========================== ========== =============
Parameter                   Authority  See also
=========================== ========== =============
Service Stitch Counter      Operator   :option:`A60`
Service Counter Reset Value Technician :option:`A61`
Service Counter Factor      Technician :option:`A62`
Service Counter Value       Technician :option:`A63`
=========================== ========== =============

Parameter List
--------------

.. option:: A60

    -Max  1
    -Min  0
    -Unit  --
    -Description
      | Active service stitch counter:
      | 0 = Off;
      | 1 = On.

.. option:: A61

    -Max  9999
    -Min  1
    -Unit  --
    -Description  Reset value of service stitch counter.

.. option:: A62

    -Max  200
    -Min  1
    -Unit  stitches
    -Description  Every sew over this number of stitches,increment the counter by 1.

.. option:: A63

    -Max  9999
    -Min  0
    -Unit  --
    -Description  The current value of service stitch counter.
