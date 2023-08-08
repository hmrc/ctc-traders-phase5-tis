These rules are the technical rules that will be used for the transition period.

During the transition period:

- the NCTS4 service will continue running to deal with in-flight transit declarations submitted before 16 November
- the NCTS5 service will handle all new declarations
- technical rules **with** Transitional Period (TP) measures will be applied to the following message types: 
  - 'Arrival Notification' E_ARR_NOT (IE007)
  - 'Declaration Amendment'  E_DEC_AMD (IE013)
  - 'Declaration Data' E_DEC_DAT (IE015)
  - 'Presentation Notification For The Pre-Lodged Declaration' E_PRE_NOT (IE170)
- technical rules **without** TP measures will be applied to all other message types  defined in this specification

**Note:** 'TPendDate' in a rule refers to 2 December 2024.