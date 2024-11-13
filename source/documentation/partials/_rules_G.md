## G0001

**Functional Description**

If at least one &lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is
EQUAL to ’30600’ in the declaration, then for the specific &lt;CONSIGNMENT-HOUSE
CONSIGNMENT&gt; the Data Group CONSIGNEE shall not be used AND &lt;CONSIGNMENT-
CONSIGNEE&gt; shall not be used. For the rest of the repetitions of &lt;CONSIGNMENT-HOUSE
CONSIGNMENT&gt; the specific IF statement (“If at least one &lt;CONSIGNMENT-HOUSE
CONSIGNMENT-ADDITIONAL INFORMATION.Code&gt; is EQUAL to ’30600’”) shall be re-validated.<br /><br />
During the Transitional Period same approach shall be followed for the &lt;CONSIGNMENT-HOUSE
CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL INFORMATION.Code&gt;.

**Technical Description**

N/A


## G0002

**Functional Description**

XSD contains a non-standard regular expression for this data item.

**Technical Description**

N/A

## G0005

**Functional Description**

The maximum value is 1999 as defined in the XSD pattern.

**Technical Description**

N/A

## G0006

**Functional Description**

&lt;TRANSPORT EQUIPMENT-GOODS REFERENCE.Declaration goods item number&gt; is filled in with
the item number of the goods concerned as provided in Declaration goods item number.

**Technical Description**

N/A


## G0009

**Functional Description**

IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {90, 93}
THEN &lt;FUNCTIONAL ERROR.Error pointer&gt; shall include the &lt;TRANSIT OPERATION.MRN&gt; of the
rejected message
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {92, 51, 52}
THEN &lt;FUNCTIONAL ERROR.Error pointer&gt; shall include the &lt;Root Element&gt;
ELSE &lt;FUNCTIONAL ERROR.Error pointer&gt; shall include the XPath location to point to the Data Item
or the Data Group that caused the error.

**Technical Description**

N/A


## G0010

**Functional Description**

IF &lt;FUNCTIONAL ERROR.Error code&gt; is EQUAL to '12'
THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Codelist number against which
validation failed (ie CLxxx)
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {13, 15}
THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Condition/Technical Rule number
against which validation failed (ie Cxxxx or Txxxx),
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is EQUAL to '14'
THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Rules/Technical Rule number against
which validation failed (ie Rxxxx or Txxxx)
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is EQUAL to '50'
THEN &lt;FUNCTIONAL ERROR.Error reason&gt; shall point to the Transitional Constraint number against
which validation failed (ie Exxxx or Bxxxx),
ELSE IF &lt;FUNCTIONAL ERROR.Error code&gt; is in SET {51, 52}
THEN the &lt;FUNCTIONAL ERROR.Error reason&gt; shall be:<br /><br />
• 'ieCAvB' if exception is thrown by ieCA
• 'NCAvB' if exception is thrown by NTA/NECA,
ELSE the &lt;FUNCTIONAL ERROR.Error reason&gt; shall have the value 'N/A'

**Technical Description**

N/A


## G0014

**Functional Description**

Eastern longitude and Northern latitude will use the optional '+' sign.<br /><br />
Western longitude and Southern latitude will use the '-' sign.

**Technical Description**

N/A


## G0015

**Functional Description**

In case of Incident information received via one or multiple CD180C, all the information received shall
be included in the D.G. &lt;CONSIGNMENT-INCIDENT&gt;.

**Technical Description**

N/A


## G0016

**Functional Description**

&lt;CONSIGNMENT-INCIDENT-TRANSPORT EQUIPMENT.Container identification number&gt; is filled in
case of incident with the new Container identification number amending initial declaration or with the
existing Container identification number if DI Number of seals is greater than 0.

**Technical Description**

N/A


## G0017

**Functional Description**

'State of seals' = ‘0’ in case that the seals are not in good state (i.e. expected but not present OR
damaged OR present with discrepancies found). In this case, the &lt;CD018C-CONTROL
RESULT.Code&gt; is ‘A5’ (or ‘B1’ if more (major) discrepancies are identified) as defined in the Transit
Manual.<br /><br />
'State of seals' = ‘1’ in case that the seals are in good state (present and not damaged, with no
discrepancies found) OR [applicable for the CD018C only] not present as expected based on
information received from other Customs Offices.

**Technical Description**

N/A


## G0020

**Functional Description**

Refers to the mode of transport corresponding to the active means of transport which is expected to be
used on exit from or entry into the Safety and Security area.

**Technical Description**

N/A


## G0021

**Functional Description**

The value '0' (zero) is a valid number in this Data Item, as per applicable XSD pattern.

**Technical Description**

N/A

## G0023

**Functional Description**

The D.I. will be filled in with new value amending initial declaration in case of incident

**Technical Description**

N/A

## G0024

**Functional Description**

D.I. will be filled if the value is provided.

**Technical Description**

N/A

## G0025

**Functional Description**

The value of D.I. &lt;CONSIGNMENT-HOUSE CONSIGNMENT.Security indicator from export
declaration&gt; will be equal to D.I. &lt;CC191C-AES RESULTS-EXPORT OPERATION.Security&gt;.

**Technical Description**

N/A


## G0026

**Functional Description**

The multiplicity of this D.G. at House Consignment level is defined as 99x for homogeneity with the
multiplicity of the same D.G. at other levels.<br /><br />
If this D.G. is used, it should be present only ONCE.<br /><br />
This D.G. can be used only in case of standard customs declaration (Additional Declaration Type = 'A')
with Export followed by Transit (Previous Document Export Type = 'N830')
(There should be maximum one export MRN included per one House Consignment, no groupage of
export declaration should be applied within one HC).

**Technical Description**

N/A


## G0029

**Functional Description**

The D.I. will be filled in with new value amending initial declaration in case of incident. In case goods
were initially not containerized and are placed in a container, or the initial container is replaced by
another container then &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is equal
to '1' else &lt;CONSIGNMENT-INCIDENT-TRANSHIPMENT.Container indicator&gt; is equal to '0'.

**Technical Description**

N/A


## G0030

**Functional Description**

If a consignment is moving from one Member State to another Member State via a third country which
is not in set of CL009 (CountryCodesCommonTransit) then a &lt;CUSTOMS OFFICE OF TRANSIT
(DECLARED)&gt; shall be declared and located in the specific Member States.

**Technical Description**

N/A


## G0033

**Functional Description**

The Data Item &lt;AUTHORISATION.Reference number&gt; must be valid in CDMS or in the National
Decision Management System.

**Technical Description**

N/A


## G0034

**Functional Description**

In case of Export followed by Transit and whenever the internal transit procedure is applied, the
Declared Office of Destination needs to be ‘appropriate’, otherwise the initial submission and/or
subsequent amendment requests of the transit declaration data as submitted by the Holder of the
Transit Procedure to the Office of Departure has to be rejected. This can be validated as follows:<br /><br />
A/ In case the Declared Office of Destination belongs to EU MS (CL010- CountryCodesCommunity),
and its Custom Office Reference Number is included in both CL172- CustomsOfficeDestination and
CL294-CustomsOfficeExitDeclared, then it is considered ‘appropriate’ (otherwise is considered not
‘appropriate’);
B/ In case the Declared Office of Destination belongs to CTC (CL112- CountryCodesCTC), it is
considered by default ‘appropriate’.
When the Declared Office of Destination is considered as not ‘appropriate’, the messages CC013C or
CC015C will be responded with CC056C that will report the error code '12- Codelist violation'.

**Technical Description**

N/A


## G0042

**Functional Description**

This D.G./D.I. is not used to report discrepancies. The Control Message always reports back D.G./D.I
as at declaration message.

**Technical Description**

N/A


## G0045

**Functional Description**

The information in this Data Group/Data Item will override the information included in the CC015C (or
in the latest CC013C, if any).

**Technical Description**

N/A


## G0050

**Functional Description**

The Reference number shall include the ARC number or the fallback eAD reference number when the
‘Type’ of the ‘Additional reference’ is C651 or C658 respectively.

**Technical Description**

N/A


## G0057

**Functional Description**

Common Code List can be extended or restricted at national level. Purely national codes are not
included in Common Domain messages.

**Technical Description**

N/A


## G0058

**Functional Description**

When &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS
DOCUMENT.Type&gt; is in SET {C651, C658} the Unique Body Reference (UBR) is required to be
recorded in this field.

**Technical Description**

N/A


## G0061

**Functional Description**

The information presented in this D.G. is related to Safety & Security and to the Binding Itinerary. In
case of Binding itinerary, the information entered must include the list of codes of the countries
between the Office of Departure and the Office of Destination. If more information is available about
the countries visited by the means of transport since it's first place of loading until the last place of
unloading, it should also be added for Safety & Security purpose only.

**Technical Description**

N/A


## G0062

**Functional Description**

The rules R0506 and R0507 are applied on CC015C and CC013C to ensure that the declaration does
not include unnecessary and repetitive information. They must be enforced by all NTA. Considering the
possibility that one Goods Item is taken out from the declaration during the control, the message
CC029C and CD001C may have different content from CC015C (or CC013C or CC170C).
Consequently, those rules R0506 and R0507 shall not be strictly enforced on the Common Domain
messages. Certainly not by the recipient of the CD message, likely not by the sender of the CD
message.

**Technical Description**

N/A


## G0068

**Functional Description**

The Data Group &lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT ITEM- ADDITIONAL
REFERENCE&gt; will be also used to include the information of EMCS consignment exported from one
EU member state into a Non-EU-Member state, in case of Export Followed by Transit (where in
messages CC013C or CC015C the &lt;CONSIGNMENT- HOUSE CONSIGNMENT- PREVIOUS
DOCUMENT.Type&gt; = ‘N830’ AND &lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT
ITEM- ADDITIONAL REFERENCE.Type&gt; is in SET CL234 (DocumentTypeExcise)).
In this case, the Data Group &lt;GOODS SHIPMENT- GOODS ITEM- PREVIOUS DOCUMENT&gt; of the
Export declaration, will be mapped with the Data Group &lt;CONSIGNMENT- HOUSE CONSIGNMENT-
CONSIGNMENT ITEM- ADDITIONAL REFERENCE&gt; of the Transit declaration.

**Technical Description**

N/A


## G0069

**Functional Description**

The Data Group &lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT ITEM- SUPPORTING
DOCUMENT&gt;, can be also used to include the information related to EMCS consignment (where
&lt;CONSIGNMENT- HOUSE CONSIGNMENT- CONSIGNMENT ITEM- SUPPORTING
DOCUMENT.Type&gt; is in SET CL234 (DocumentTypeExcise)), transported from one EU member state
into another EU member state via a CTC country.

**Technical Description**

N/A


## G0071

**Functional Description**

In case of Export Followed by Transit (i.e. &lt;CONSIGNMENT-HOUSE CONSIGNMENT- PREVIOUS
DOCUMENT.Type&gt; = ‘N830’), all and only the goods items declared in &lt;GOODS SHIPMENT-GOODS
ITEM&gt; as defined in the related Export declaration (identified by the MRN) must be included in
&lt;CONSIGNMENT-HOUSE CONSIGNMENT- CONSIGNMENT ITEM&gt; Data Group.

**Technical Description**

N/A


## G0072

**Functional Description**

In case of Export Followed By Transit (&lt;CONSIGNMENT-HOUSE CONSIGNMENT- PREVIOUS
DOCUMENT.Type&gt; = ‘N830’),
-   all the goods items declared in &lt;GOODS SHIPMENT-GOODS ITEM&gt; as defined in the related Export
declaration (identified by the MRN) and
-   all the goods items declared in the &lt;CONSIGNMENT-HOUSE CONSIGNMENT- CONSIGNMENT
ITEM&gt; defined in the transit declaration
must be listed in the same order (with &lt;GOODS SHIPMENT-GOODS ITEM.Declaration goods item
number&gt; = &lt;CONSIGNMENT-HOUSE CONSIGNMENT- CONSIGNMENT ITEM.Goods item
number&gt;). Keeping the order of the goods item is required to enable the automatic validation of the
matching of the goods in the context of Export followed by Transit.

**Technical Description**

N/A


## G0088

**Functional Description**

When &lt;CONSIGNMENT.Inland mode of transport&gt; is EQUAL to '3', the identification number of the
trailer must also be provided (where applicable).

**Technical Description**

N/A


## G0090

**Functional Description**

The Data Group ‘Carrier’ shall be provided if the value is different from the ‘Holder of the transit
procedure’.
The Data Group ‘Carrier’ should not be present if the ‘Holder of the transit procedure’ is also the
‘Carrier’.

**Technical Description**

N/A


## G0101

**Functional Description**

The value of the Data Item &lt;INVALIDATION.Initiated by customs&gt; is
 ‘0’ ('No') when the request to invalidate is initiated by the trader;
The value of the Data Item &lt;INVALIDATION.Initiated by customs&gt; is
 ‘1’ ('Yes') when the request to invalidate is initiated by the customs.

**Technical Description**

N/A


## G0102

**Functional Description**

For each type of authorisation, the authorisation is valid for the whole declaration (i.e. for the different
HOUSE CONSIGNMENTS).

**Technical Description**

N/A


## G0103

**Functional Description**

Each iteration of this data group shall include:<br /><br />
-Either the transport equipment information for the containerised goods with seals OR without seals
with reference to those goods;
-OR the transport equipment information for the non containerised but sealed goods (e.g. goods
carried by truck with seals) with reference to those goods;
Note: the non containerised and unsealed goods shall not be recorded under this data group.

**Technical Description**

N/A


## G0105

**Functional Description**

Information recorded under this data group is solely for communication purposes. No legal liabilities
exist upon the specific contact person.

**Technical Description**

N/A


## G0112

**Functional Description**

If IMO ship identification number (type ‘10’) exists for that ship, it must be used and the Name of the
sea-going vessel (type ‘11’) shall not be used.

**Technical Description**

N/A


## G0113

**Functional Description**

The country code used to define the ‘Country of destination’ can be different from the country code
used in the data item ‘Country’ included in the address of the ‘Consignee’.

**Technical Description**

N/A


## G0114

**Functional Description**

The Data Item &lt;AUTHORISATION.Type&gt; shall include the value ‘C521’ when the transit declaration is
submitted under simplified procedure (authorised consignor) and only in this case.

**Technical Description**

N/A


## G0115

**Functional Description**

This Data Item is required as per UCC-DA (Annex B) but may be waived for modes of transport other
than rail in case the transit movement does not cross the external border of the Union.

**Technical Description**

N/A


## G0117

**Functional Description**

Common Code List can be extended at national level. Purely national codes are not included in
Common Domain messages.

**Technical Description**

N/A


## G0118

**Functional Description**

IF the declaration is lodged without Safety and Security data then:<br /><br />
-where goods are carried in multimodal transport units, such as containers, swap bodies and semi
trailers, the customs authorities may authorise the holder of the transit procedure not to provide this
information where the logistical pattern at the point of departure may prevent the identity and
nationality of the means of transport from being provided at the time the goods are released for transit,
providing multimodal transport units bear unique numbers and such numbers are indicated in D.E. 19
07 063 000 Container identification number
-In the following cases, Member States shall waive the obligation to enter this information on a transit
declaration lodged at the office of departure in relation with the means of transport on which the goods
are directly loaded:<br /><br />
  -where the logistical pattern does not allow this data element to be provided and the holder of the
transit procedure has the AEOC status and
   -where the relevant information may be traced where needed by the customs authorities via the
records of the holder of the transit procedure.

**Technical Description**

N/A


## G0119

**Functional Description**

This Data Group is “Required” except where one of the following conditions apply:<br /><br />
-For the declaration that include Inland Mode Of Transport with the value ‘5’;
-Where goods are carried in multimodal transport units, such as containers, swap bodies and semi
trailers, the customs authorities may authorise the holder of the transit procedure not to provide this
information where the logistical pattern at the point of departure may prevent the identity and
nationality of the means of transport from being provided at the time the goods are released for transit,
providing multimodal transport units bear unique numbers and such numbers are indicated in the Data
Item ‘Container identification number’;
-For the means of transport on which the goods are directly loaded:<br /><br />
-the logistical pattern does not allow this data element to be provided and the holder of the transit
procedure has the appropriate status (AEOC in EU) and
-the relevant information may be traced where needed by the customs authorities via the records of
the holder of the transit procedure.

**Technical Description**

N/A


## G0120

**Functional Description**

The Data Item ‘Identification number’ is required for the Data Group ‘HOLDER OF THE TRANSIT
PROCEDURE’, except for:<br /><br />
- economic operators residing outside of the common transit countries (outside CL009), and
- private individuals for which an identification number may be used but is not required.

**Technical Description**

N/A


## G0123

**Functional Description**

This Data Group must be provided when different from the ‘HOLDER OF THE TRANSIT
PROCEDURE’.
IF the unique ‘CONSIGNOR’ of the consignment is different from the ‘HOLDER OF THE TRANSIT
PROCEDURE’
THEN the Data Group &lt;CONSIGNMENT -CONSIGNOR&gt; must include this ‘CONSIGNOR’;
IF the ‘CONSIGNOR’ of one or more house consignment(s) is different from the ‘HOLDER OF THE
TRANSIT PROCEDURE’
THEN the Data Group &lt;CONSIGNMENT -HOUSE CONSIGNMENT -CONSIGNOR&gt; must include this
‘CONSIGNOR’.

**Technical Description**

N/A


## G0126

**Functional Description**

The value of this Data Item should be:<br /><br />
‘A1’ (Satisfactory): When the goods are released for transit after physical control (full or partial) and no
discrepancies were detected;
‘A2’ (Considered satisfactory): When the goods are released for transit after documentary control only
(no physical control) and no discrepancies were detected or without any control;
‘A3’ (Simplified procedure): In case of simplified procedure without control performed by the Customs
Office of Departure (the goods are released for transit by an authorised consignor).

**Technical Description**

N/A


## G0127

**Functional Description**

The Data Item shall be filled, by using the information of the &lt;TRANSIT OPERATION. Limit date&gt;,
included either:<br /><br />
- in the initial declaration CC015C message or
- in any possible amendments CC013C or
- using the revised expected arrival date entered by the Officer at the Office Of Departure when the
movement is released for transit.

**Technical Description**

N/A


## G0131

**Functional Description**

IF discrepancies have been found the Data Group will be filled in with new values amending initial
declaration.

**Technical Description**

N/A


## G0139

**Functional Description**

The ‘0’ (zero) value should only be used in cases where the customs officer identifies that two or more
goods items are packaged together but this was not declared correctly at first instance.

**Technical Description**

N/A


## G0142

**Functional Description**

&lt;CUSTOMS OFFICE OF TRANSIT (DECLARED)&gt; shall be declared when switching from a
contracting party to a different contracting party.

**Technical Description**

N/A


## G0160

**Functional Description**

If the declaration is submitted under simplified procedure then this D.G/D.I. must be present.

**Technical Description**

N/A

## G0165

**Functional Description**

IF the declaration is submitted under simplified procedure AND the authorisation of which foresees the
use of seals,
THEN &lt;CONSIGNMENT-TRANSPORT EQUIPMENT.Number of seals&gt; is GREATER than '0'.

**Technical Description**

N/A


## G0167

**Functional Description**

In case of pre-lodged declaration, the Authorisation should be still valid until the PRESENTATION
NOTIFICATION FOR THE PRE-LODGED DECLARATION message (CC170C) is submitted when it
will be revalidated.

**Technical Description**

N/A


## G0186

**Functional Description**

&lt;UNLOADING REMARK.Unloading completion&gt; is used as a flag and it can contain 2 possible values:<br /><br />
 ‘0’ = ‘NO’ This means that the unloading of the goods is not yet completed;
 ‘1’ = ‘YES’ This means that the goods are completely unloaded.

**Technical Description**

N/A

## G0196

**Functional Description**

This data group must contain the full transport equipment details and not only what is different
compared to the data declared in the customs declaration.

**Technical Description**

N/A


## G0201

**Functional Description**

Rule R0840 shall be validated only by MS. IF the sender is a CTC country THEN the &lt;CUSTOMS
OFFICE OF TRANSIT&gt; in MS, that detects the violation of R0840, should request a new ENS
declaration before it authorizes the goods to enter the EU. The message CD050C or CD115C from a
CTC country may not be rejected if R0840 is violated.

**Technical Description**

N/A


## G0205

**Functional Description**

&lt;UNLOADING REMARK.Conform&gt; is used as a flag and it can contain 2 possible values:<br /><br />
   ‘0’ = ‘NO’ there are unloading remarks;
   ‘1’ = ‘YES’ no unloading remarks present.

**Technical Description**

N/A

## G0217

**Functional Description**

From the originally received IE, only the D.G./D.I. in error are transmitted back to the Trader, indicating
whether the D.G./D.I. in question is (are) missing or incorrect.

**Technical Description**

N/A


## G0300

**Functional Description**

The UN Number must be present if the commodity includes dangerous goods that are listed in the
United Nations Dangerous Goods Code (UNDG).

**Technical Description**

N/A


## G0301

**Functional Description**

The Data Item &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-
COMMODITY.CUS code&gt; can be used when the CL016 (CUSCode) in CS/RD2 includes [CUS code &
CN code] where the CN code matches with the &lt;CONSIGNMENT-HOUSE CONSIGNMENT-
CONSIGNMENT ITEM-COMMODITY-COMMODITY CODE. Harmonized System sub-heading code&gt;
& &lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-COMMODITY-COMMODITY
CODE.Combined nomenclature code&gt;.

**Technical Description**

N/A


## G0321

**Functional Description**

This Data Item can take the value '0' (zero) in the following cases:<br /><br />
a. a document number is missing (i.e. it shall not be filled in with a dummy number);
b. the length of a document number exceeds the allowed 70 characters (i.e. it shall not be truncated).
A missing document reference number (due to the above or any other case) is not a valid reason for
the rejection of this message.

**Technical Description**

N/A


## G0332

**Functional Description**

IF &lt;Container indicator&gt; is NOT PRESENT then data group &lt;TRANSPORT EQUIPMENT&gt; shall NOT
be PRESENT, too. &lt;Container indicator&gt; functions as the governing data item for data group
&lt;TRANSPORT EQUIPMENT&gt;.

**Technical Description**

N/A


## G0360

**Functional Description**

IF discrepancies have been found in one or more Data Groups or Data Items
OR
a new data element has been found during the control
THEN the D.G. / D.I.= "R" and is used to report these discrepancies
ELSE the D.G. / D.I. = "N".

**Technical Description**

N/A


## G0414

**Functional Description**

In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT
ITEM.SUPPORTING DOCUMENT.Type&gt; is EQUAL to 'C651 -AAD -Administrative Accompanying
Document (EMCS)', the Administrative Reference Code (ARC number) shall be recorded in this field;
In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT
ITEM.SUPPORTING DOCUMENT.Type&gt; is EQUAL to 'C658 -FAD -Fallback e-AD (EMCS)', the
national Fallback registration number shall be recorded in this field.

**Technical Description**

N/A


## G0424

**Functional Description**

In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT
ITEM.ADDITIONAL REFERENCE.Type&gt; is EQUAL to 'C651 -AAD -Administrative Accompanying
Document (EMCS)', the
Administrative Reference Code (ARC number) shall be recorded in this field;
In case of excise goods where &lt;CONSIGNMENT.HOUSE CONSIGNMENT.CONSIGNMENT
ITEM.ADDITIONAL REFERENCE.Type&gt; is EQUAL to 'C658C -FAD -Fallback e-AD (EMCS)’, the
national Fallback registration number shall be recorded in this field.

**Technical Description**

N/A


## G0500

**Functional Description**

The exact content of the CL326 (QualifierOfTheIdentification) is defined nationally, considering -for
example -that only in some NAs the value 'T' must only be used in case “House number” and
“Postcode” or only “Postcode” define an exact and unique location.

**Technical Description**

N/A


## G0510

**Functional Description**

When the &lt;CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; indicates the permission to start the
unloading, all the information about the Consignment is provided.<br /><br />
When the &lt;CUSTOMS OFFICE OF DESTINATION (ACTUAL)&gt; indicates the permission to continue
the unloading, the information about the Consignment is not provided, and the Data Item
&lt;CTL_CONTROL.Continue unloading&gt; shall be used with an incremental value ('1', '2', '3', etc ...) in
the subsequent messages CC043C (one message for each authorisation to continue the unloading).

**Technical Description**

N/A


## G0587

**Functional Description**

The Customs Office of Exit for Transit shall be provided - in case of transit declaration combined with
EXS - when the goods will exit the Security Area to enter (or re-enter) a CTC country that is not in the
Security Area.

**Technical Description**

N/A


## G0670

**Functional Description**

If all goods items are related a single container, the data group can be omitted.<br /><br />
Otherwise all the goods items related to this container (if present) must be declared.<br /><br />
All the non-containerised goods items related to this seals information (if present) must be declared as
well.

**Technical Description**

N/A


## G0789

**Functional Description**

The ’Customs office at border reference number’ identifies the border crossing point (BCP) where the
‘Active border transport means’ will be present. It is either the ‘Reference number’ of one of the
‘CUSTOMS OFFICE OF TRANSIT (DECLARED)’ or the ‘Reference number’ of one of the ‘CUSTOMS
OFFICE OF EXIT FOR TRANSIT (DECLARED)’ or the ‘Reference number’ of the ‘CUSTOMS OFFICE
OF DESTINATION (DECLARED)’. By using this Data Item, it is possible (after the end of the
Transitional Period) to identify which transport means will be present at which border crossing point, in
case of multiple BCP and multiple changes of active transport means.

**Technical Description**

N/A


## G0825

**Functional Description**

- Consignment related information shall be recorded under
&lt;CONSIGNMENT-ADDITIONAL SUPPLY CHAIN ACTOR&gt;
&lt;CONSIGNMENT-PREVIOUS DOCUMENT&gt;
&lt;CONSIGNMENT-SUPPORTING DOCUMENT&gt;
&lt;CONSIGNMENT-TRANSPORT DOCUMENT&gt;
&lt;CONSIGNMENT-ADDITIONAL REFERENCE&gt;
&lt;CONSIGNMENT-ADDITIONAL INFORMATION&gt;
- House Consignment related information shall be recorded under+
&lt;CONSIGNMENT-HOUSE CONSIGNMENT- ADDITIONAL SUPPLY CHAIN ACTOR&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-PREVIOUS DOCUMENT&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-SUPPORTING DOCUMENT&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-TRANSPORT DOCUMENT&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL REFERENCE&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-ADDITIONAL INFORMATION&gt;
- Goods item related information shall be recorded under
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL SUPPLY CHAIN
ACTOR&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-PREVIOUS DOCUMENT&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-SUPPORTING DOCUMENT&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL REFERENCE&gt;
&lt;CONSIGNMENT-HOUSE CONSIGNMENT-CONSIGNMENT ITEM-ADDITIONAL INFORMATION&gt;

**Technical Description**

N/A


## G0850

**Functional Description**

This Data Group must be filled in if a &lt;REPRESENTATIVE&gt; is used by the &lt;HOLDER OF THE
TRANSIT PROCEDURE&gt;.

**Technical Description**

N/A


## G0860

**Functional Description**

This Data Group must be filled in if the Data Group &lt;REPRESENTATIVE&gt; was used in the preceding
message that was received by the &lt;CUSTOMS OFFICE OF DEPARTURE&gt;.

**Technical Description**

N/A


## G0868

**Functional Description**

The data recorded under this data group must be exactly the same as in the respective data group of
the preceding message that is received.

**Technical Description**

N/A


## G0988

**Functional Description**

The Country of dispatch can be different from the Country defined in the address of the Consignor.

**Technical Description**

N/A

## G0989

**Functional Description**

This Data Group is inserted as transitional but without any transitional measure applied to it. The Data
Group is present in this message, in order to ensure consistency of the structure across the lifecycle of
the movements during the Transitional Period.<br /><br />
This Guideline aims to draw the attention on the potential need for Technical Rules for Transition
(Exxxx) or Business Rules for Transition (B1xxx and B2xxx) as defined in the section “1. Introduction”
of DDNTA APPENDIX Q2.

**Technical Description**

N/A


## G0991

**Functional Description**

During the Transitional Period, the value ‘N830’ (Goods declaration for exportation) is defined as valid
in codelist CL214 (PreviousDocumentType). From the end date of the Transitional Period, the value
‘N830’ will become valid ONLY in the CL228 (PreviousDocumentExportType) to indicate the “Export
Followed by Transit” procedure in the Data Group &lt;CONSIGNMENT-HOUSE CONSIGNMENT&gt;.

**Technical Description**

N/A
