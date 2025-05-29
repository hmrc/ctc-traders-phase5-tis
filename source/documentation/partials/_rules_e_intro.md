These rules are the technical rules that will be used for the transition period.

During the transition period:

- the NCTS5 service will handle all new declarations
- technical rules **with** Transitional Period (TP) measures will be applied to the following message types: 
  - 'Arrival Notification' E_ARR_NOT (IE007)
  - 'Declaration Amendment'  E_DEC_AMD (IE013)
  - 'Declaration Data' E_DEC_DAT (IE015)
  - 'Presentation Notification For The Pre-Lodged Declaration' E_PRE_NOT (IE170)
- technical rules **without** TP measures will be applied to all other message types  defined in this specification

**Note:** For information about the go-live of the UK NCTS5 service and the 'TPendDate', see [NCTS5 key dates](/guides/ctc-traders-phase5-tis/#ncts5-key-dates).