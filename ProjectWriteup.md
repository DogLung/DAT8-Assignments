**What is the question you hope to answer?**

*Can I predict the type of product complaint based on the percentages of Income, Born in State of Residence, Foreign Born, and Poverty Status of a given Zipcode/ZCTA?*

Given that I am not a subject matter expert, some of the factors may be found to be irrelevant.  Other sources may be found in the process of this project, but the scope will adjust as needed.

**What data are you planning to use to answer that question?**

Since this project is based off an given skills assessment test from the Consumer Financial Protection Bureau, the datasets instructions that were provided are the following:

For this exercise you are to build a script or program based in the following instructions:

  1.    Download CFPB’s public complaint database (http://www.consumerfinance.gov/complaintdatabase/)

  2.    Download income data from the 5-year ACS survey file from census.gov (http://www2.census.gov/acs2013_5yr/summaryfile/2009-2013_ACSSF_By_State_By_Sequence_Table_Subset/UnitedStates/All_Geographies_Not_Tracts_Block_Groups/20135us0015000.zip) 

  The header information for the sequence file can be found in the Seq15.xls file in the zip file located here:  http://www2.census.gov/programs-surveys/acs/summary_file/2013/data/2013_5yr_Summary_FileTemplates.zip.
  3. Download geography information for the 5-year ACS survey file from census.gov (http://www2.census.gov/acs2013_5yr/summaryfile/2009-2013_ACSSF_By_State_By_Sequence_Table_Subset/UnitedStates/All_Geographies_Not_Tracts_Block_Groups/g20135us.csv)

  The header information for the geography file can be found on page 10 of the technical document here:  http://www2.census.gov/acs2013_5yr/summaryfile/ACS_2013_SF_Tech_Doc.pdf

**What do you know about the data so far?**

What I know about the data so far is that the types of complaints can be very granualar if needed, much of it can probably be aggregated when needed.  The headers for the data are in different formats for the various files.  The complaint database seems to be very robust, but the geography information can be a bit sparse for particular columns.  A lot of filtering and cleaning may need to be applied in such cases.  There is a likely possibility that an altnerative datasource would provide a better starting point, but for now this current source will be good practice.  Other geographic data can be appended to the project if found relevant.

**Why did you choose this topic?**

This topic is based upon a skills assessment that I was given when applying to the Consumer Financial Protection Bureau.  At the time I was trying to teach myself Python on the fly while taking the assessment.  I did not complete it, as I was not keen to the techniques of cleaning nor experienced with machine learning.  However, I hope to be able to accomplish the tesk utilizing the skills I learn in this class.
