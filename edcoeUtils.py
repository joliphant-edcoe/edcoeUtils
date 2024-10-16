import os
import pandas as pd


# 'name' : 'ca district code'
district_codes = {
    "black_oak_mine_unified": "0973783",
    "buckeye_unified": "0961838",
    "camino_unified": "0961846",
    "el_dorado_county_office_of_education": "0910090",
    "el_dorado_union_high": "0961853",
    "gold_oak_union_elementary": "0961879",
    "gold_trail_union_elementary": "0961887",
    "indian_diggings_elementary": "0961895",
    "lake_tahoe_unified": "0961903",
    "latrobe": "0961911",
    "mother_lode_union_elementary": "0961929",
    "pioneer_union_elementary": "0961945",
    "placerville_union_elementary": "0961952",
    "pollock_pines_elementary": "0961960",
    "rescue_union_elementary": "0961978",
    "silver_fork_elementary": "0961986",
}

district_acronym = {
    "black_oak_mine_unified": "BOM",
    "buckeye_unified": "BUSD",
    "camino_unified": "CUSD",
    "el_dorado_county_office_of_education": "EDCOE",
    "el_dorado_union_high": "EDUHSD",
    "gold_oak_union_elementary": "GOUSD",
    "gold_trail_union_elementary": "GTUSD",
    "indian_diggings_elementary": "",
    "lake_tahoe_unified": "LTUSD",
    "latrobe": "LAT",
    "mother_lode_union_elementary": "MLUSD",
    "pioneer_union_elementary": "PIO",
    "placerville_union_elementary": "PUESD",
    "pollock_pines_elementary": "PPESD",
    "rescue_union_elementary": "RUSD",
    "silver_fork_elementary": "SFESD",
}

district_names = dict((v, k) for k, v in district_codes.items())


def get_district_code(d_name: str) -> str:
    return district_codes.get(d_name)


def get_district_name(code: str) -> str:
    return district_names.get(code)


def get_formatted_district_name(code: str) -> str:
    if not district_names.get(code):
        return None
    return district_names.get(code).replace("_", " ").title()


# CA district code : NCES (US) code
NCES_codes = {
    "0973783": "0605240",
    "0961838": "0606270",
    "0961846": "0607170",
    "0910090": "0691006",
    "0961853": "0612070",
    "0961879": "0615390",
    "0961887": "0615450",
    "0961895": "0618240",
    "0961903": "0620640",
    "0961911": "0621180",
    "0961929": "0625980",
    "0961945": "0630480",
    "0961952": "0630780",
    "0961960": "0631290",
    "0961978": "0632310",
    "0961986": "0636810",
}


CAdistrict_codes = dict((v, k) for k, v in NCES_codes.items())


def convert_to_NCSE(district_code: str) -> str:
    return NCES_codes.get(district_code)


def convert_to_CAdistrict(NCES_code: str) -> str:
    return CAdistrict_codes.get(NCES_code)


# in Aeries
edcoe_schools = {
    0: "EDCOE",
    111: "Blue Ridge Court School",
    99: "Charter Collge & Career Prep",
    52: "Charter Connections Academy",
    51: "Charter Home Study Academy",
    54: "Charter University Prep",
    100: "Mountainside Adult Education",
    150: "Mountainside Middle College High School",
    101: "Mountainside Success Academy",
    53: "Rite of Passage Qualifying House",
    57: "Rite of Passage Sierra Ridge Academy",
    68: "Special Services",
    73: "Special Services Adult Transition",
    72: "Special Services High - UMHS",
    70: "Special Services High",
    60: "Special Services Infants & Toddlers",
    69: "Special Services Middle",
    1: "Special Services NPS LCI",
    61: "Special Services Preschool",
}

# expected schools CBEDS
edcoe_school_codes = {
    "0106047": "Blue Ridge",
    "0930016": "Golden Ridge",
    "0123521": "Charter Home Study Academy",
    "0930123": "Mountainside Middle College High School",
    "0930131": "Rite of Passage",
    "6069470": "Special Services",
    "0136036": "John Adams Academy - El Dorado Hills",
}


def get_school_name(school_number):
    return edcoe_schools.get(school_number)


extractColumns = {
    "CRSC": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofCourseDelivery",
        "AcademicYearID",
        "CRS-StateCourseCode",
        "CRS-LocalCourseID",
        "CRS-CourseName",
        "Filler",
        "Filler.1",
        "CRS-CTEPostsecondaryArticulatedCourseIndicator",
        "CRS-UCCSUApprovedIndicator",
        "CourseSectionID",
        "AcademicTermCode",
        "SEID",
        "LocalStaffID",
        "ClassID",
        "CourseSectionInstructionalLevelCode",
        "EducationServiceCode",
        "LanguageofInstructionCode",
        "InstructionalStrategyCode",
        "IndependentStudyIndicator",
        "DistanceLearningIndicator",
        "MultipleTeacherCode",
        "EducationProgramFundingSourceCode",
        "CTECourseSectionProviderCode",
        "CourseContentAreaSubcategoryCode",
        "CRS-DepartmentalizedCourseStandardsGradeLevelRangeCode",
        "CRS-ContentStandardsAlignmentCode",
        "Filler.2",
        "AP/IBCourseCodeCrossReference",
        "OnlineCourseInstructionTypeCode",
        "MiddleSchoolCoreSettingIndicator",
        "LocalAssignmentOptionCode",
        "HighQualityCTECourseIndicator",
    ],
    "CRSE": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofCourseDelivery",
        "AcademicYearID",
        "CRS-StateCourseCode",
        "CRS-LocalCourseID",
        "CRS-CourseName",
        "Filler",
        "Filler.1",
        "CRS-CTEPostsecondaryArticulatedCourseIndicator",
        "CRS-UCCSUApprovedIndicator",
        "CourseSectionID",
        "AcademicTermCode",
        "SEID",
        "LocalStaffID",
        "ClassID",
        "CourseSectionInstructionalLevelCode",
        "EducationServiceCode",
        "LanguageofInstructionCode",
        "InstructionalStrategyCode",
        "IndependentStudyIndicator",
        "DistanceLearningIndicator",
        "MultipleTeacherCode",
        "EducationProgramFundingSourceCode",
        "CTECourseSectionProviderCode",
        "CourseContentAreaSubcategoryCode",
        "CRS-DepartmentalizedCourseStandardsGradeLevelRangeCode",
        "CRS-ContentStandardsAlignmentCode",
        "Filler.2",
        "AP/IBCourseCodeCrossReference",
        "OnlineCourseInstructionTypeCode",
        "MiddleSchoolCoreSettingIndicator",
        "LocalAssignmentOptionCode",
        "HighQualityCTECourseIndicator",
    ],
    "MEET": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "LocalSpecialEducationStudentID",
        "ReportingSELPA",
        "SpecialEducationReferralDate",
        "ReferringPartyCode",
        "InitialEvaluationParentalConsentDate",
        "SpecialEducationMeetingDate",
        "PendingAsOfDate",
        "MeetingDelayCode",
        "MeetingActivity-EvaluationTypeCode",
        "MeetingActivity-PlanReviewIndicator",
        "EvaluationOutcomeCode",
        "ParentalInvolvementFacilitationCode",
    ],
    "PLAN": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "LocalSpecialEducationStudentID",
        "ReportingSELPA",
        "DistrictofSpecialEducationAccountability",
        "SpecialEducationPlanTypeCode",
        "SpecialEducationPlanEffectiveStartDate",
        "ReasonForPlanRecordCode",
        "PrimaryResidenceCode",
        "Disability1Code",
        "Disability1DegreeofSupport",
        "Disability2Code",
        "Disability2DegreeofSupport",
        "InfantRegionalCenterServicesEligibilityIndicator",
        "SpecialEducationProgramSettingCode",
        "PreschoolProgramSettingServiceLocationCode",
        "TenorMoreWeeklyHoursinSettingIndicator",
        "GeneralEducationParticipationPercentage",
        "SpecialEducationProgramTypeCode",
        "IEPIncludesPostsecondaryGoalsIndicator",
        "PostsecondaryGoalsUpdatedAnnuallyIndicator",
        "PostsecondaryGoalsAgeAppropriateTransitionAssessmentIndicator",
        "TransitionServicesinIEPIndicator",
        "SupportiveServicesIndicator",
        "TransitionServicesGoalsinIEPIndicator",
        "StudentIEPParticipationIndicator",
        "AgencyRepresentativeIEPParticipationCode",
        "SpecialTransportationIndicator",
    ],
    "PSTS": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "SchoolofAttendanceNPS",
        "AcademicYearID",
        "SSID",
        "LocalSpecialEducationStudentID",
        "ReportingSELPA",
        "EducationProgramParticipationTypeCode",
        "PostsecondaryStatusCode",
        "EducationalInstitutionType",
        "IndustryField",
        "Post-HighSchoolCredential",
    ],
    "SASS": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAssignment",
        "AcademicYearID",
        "SEID",
        "LocalStaffID",
        "StaffLegalFirstName",
        "StaffLegalLastName",
        "StaffBirthDate",
        "StaffGenderCode",
        "StaffJobClassificationCode",
        "StaffJobClassificationFTEPercentage",
        "NonClassroomBasedJobAssignmentCode1",
        "NonClassroomBasedJobAssignmentCode2",
        "NonClassroomBasedJobAssignmentCode3",
        "NonClassroomBasedJobAssignmentCode4",
        "NonClassroomBasedJobAssignmentCode5",
        "NonClassroomBasedJobAssignmentCode6",
        "NonClassroomBasedJobAssignmentCode7",
    ],
    "SCSC": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofCourseDelivery",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "LocalCourseID",
        "CourseSectionID",
        "AcademicTermCode",
        "StudentCreditsAttempted",
        "StudentCreditsEarned",
        "StudentCourseFinalGrade",
        "UC/CSUAdmissionRequirementCode",
        "MarkingPeriod",
        "CarnegieUnitsEarned",
    ],
    "SCSE": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofCourseDelivery",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "LocalCourseID",
        "CourseSectionID",
        "AcademicTermCode",
        "StudentCreditsAttempted",
        "StudentCreditsEarned",
        "StudentCourseFinalGrade",
        "UC/CSUAdmissionRequirementCode",
        "MarkingPeriod",
        "CarnegieUnitsEarned",
    ],
    "SCTE": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "CTEPathwayCode",
        "CTEPathwayCompletionAcademicYearID",
    ],
    "SDEM": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "EffectiveStartDate",
        "EffectiveEndDate",
        "ReportingLEA",
        "AcademicYearID",
        "SEID",
        "LocalStaffID",
        "StaffLegalFirstName",
        "StaffLegalMiddleName",
        "StaffLegalLastName",
        "StaffAliasFirstName",
        "StaffAliasMiddleName",
        "StaffAliasLastName",
        "StaffBirthDate",
        "StaffGenderCode",
        "StaffHispanicEthnicityIndicator",
        "StaffEthnicityMissingIndicator",
        "StaffRace1Code",
        "StaffRace2Code",
        "StaffRace3Code",
        "StaffRace4Code",
        "StaffRace5Code",
        "StaffRaceMissingIndicator",
        "StaffHighestDegreeCode",
        "StaffEmploymentStatusCode",
        "StaffEmploymentStartDate",
        "StaffEmploymentEndDate",
        "StaffServiceYearsLEA",
        "StaffServiceYearsTotal",
    ],
    "SDIS": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "DisciplinaryIncidentIDLocal",
        "DisciplinaryIncidentOccurrenceDate",
        "StudentOffenseCode",
        "IncidentMostSevereOffenseCode",
        "WeaponCategoryCode",
        "IncidentDisciplinaryActionTakenCode",
        "DisciplinaryActionAuthorityCode",
        "IncidentDisciplinaryActionDurationDays",
        "StudentInstructionalSupportIndicator",
        "ExpulsionModificationCategoryCode",
        "RemovaltoInterimAlternativeSettingReasonCode",
    ],
    "SELA": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "LocalStudentID",
        "EnglishLanguageAcquisitionStatusCode",
        "EnglishLanguageAcquisitionStatusStartDate",
        "PrimaryLanguageCode",
    ],
    "SENR": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "SchoolofAttendanceNPS",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalMiddleName",
        "StudentLegalLastName",
        "StudentLegalNameSuffix",
        "StudentAliasFirstName",
        "StudentAliasMiddleName",
        "StudentAliasLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "StudentBirthCity",
        "StudentBirthStateProvinceCode",
        "StudentBirthCountryCode",
        "EnrollmentStartDate",
        "EnrollmentStatusCode",
        "GradeLevelCode",
        "EnrollmentExitDate",
        "StudentExitReasonCode",
        "StudentSchoolCompletionStatus",
        "ExpectedReceiverSchoolofAttendance",
        "StudentMetallUCCSURequirementsIndicator",
        "StudentSchoolTransferCode",
        "DistrictofGeographicResidenceCode",
        "MeritDiplomaIndicator",
        "SealofBiliteracyIndicator",
        "AdultAgeStudentswithDisabilitiesinTransitionStatus",
        "GraduationExemptionIndicator",
    ],
    "SERV": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "NonpublicAgencyIdentifier(NPA)",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "ReportingSELPA",
        "DistrictofSpecialEducationAccountability",
        "SpecialEducationServiceCode",
        "SpecialEducationServiceProviderCode",
        "SpecialEducationServiceLocationCode",
        "ServiceFrequencyCode",
        "ServiceDuration",
        "LocalSpecialEducationStudentID",
        "PlanEffectiveStartDate",
    ],
    "SINC": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "IncidentIDLocal",
        "IncidentOccurrenceDate",
        "StatutoryOffenseIndicator",
        "StudentInstructionalSupportIndicator",
        "RemovaltoInterimAlternativeSettingReasonCode",
    ],
    "SINF": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "EffectiveStartDate",
        "EffectiveEndDate",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalMiddleName",
        "StudentLegalLastName",
        "StudentLegalNameSuffixCode",
        "StudentAliasFirstName",
        "StudentAliasMiddleName",
        "StudentAliasLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "StudentBirthCity",
        "StudentBirthStateProvinceCode",
        "StudentBirthCountryCode",
        "StudentHispanicEthnicityIndicator",
        "StudentEthnicityMissingIndicator",
        "StudentRace1Code",
        "StudentRace2Code",
        "StudentRace3Code",
        "StudentRace4Code",
        "StudentRace5Code",
        "StudentRaceMissingIndicator",
        "ResidentialAddressLine1",
        "ResidentialAddressLine2",
        "ResidentialAddressCityName",
        "ResidentialAddressStateProvinceCode",
        "ResidentialAddressZipCode",
        "StudentInitialUSSchoolEnrollmentDateK-12",
        "EnrolledinUSSchoollessthanThreeCumulativeYearsIndicator",
        "ParentGuardian1HighestEducationLevelCode",
        "Guardian1FirstName",
        "Guardian1LastName",
        "Guardian2FirstName",
        "Guardian2LastName",
        "StudentPreferredFirstName",
        "StudentPreferredLastName",
        "MailingAddressLine1",
        "MailingAddressLine2",
        "MailingAddressCityName",
        "MailingAddressStateProvinceCode",
        "MailingAddressZipCode",
        "ParentGuardian2HighestEducationLevelCode",
    ],
    "SIRS": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "IncidentIDLocal",
        "IncidentResultCode",
        "IncidentResultAuthorityCode",
        "IncidentResultsDurationDays",
        "IncidentResultModificationCode",
    ],
    "SOFF": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "IncidentIDLocal",
        "StudentOffenseCode",
        "WeaponCategoryCode",
    ],
    "SPRG": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "StudentLegalFirstName",
        "StudentLegalLastName",
        "StudentBirthDate",
        "StudentGenderCode",
        "EducationProgramCode",
        "EducationProgramMembershipCode",
        "EducationProgramMembershipStartDate",
        "EducationProgramMembershipEndDate",
        "EducationServiceAcademicYear",
        "EducationServiceCode",
        "CaliforniaPartnershipAcademyID",
        "MigrantStudentID",
        "Filler",
        "Filler.1",
        "HomelessDwellingType",
        "UnaccompaniedYouthIndicator",
        "Filler.2",
        "Filler.3",
    ],
    "STAS": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "Filler",
        "Filler.1",
        "Filler.2",
        "Filler.3",
        "StudentAbsenceSummaryDataCollectionExemptionIndicator",
        "HourlyAttendanceSchoolTypeIndicator",
        "ExpectedAttendanceDays",
        "DaysAttendedIn-Person",
        "DaysAbsentOut-of-SchoolSuspension",
        "DaysinAttendanceIn-SchoolSuspension",
        "DaysAbsentIn-PersonExcusedNon-Suspension",
        "DaysAbsentIn-PersonUnexcusedNon-Suspension",
        "Non-ADAGeneratingIndependentStudyDays",
        "ADAGeneratingIndependentStudyDays",
        "Period-by-PeriodAttendanceMethodIndicator",
    ],
    "SWDS": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "AcademicYearID",
        "SSID",
        "LocalStudentID",
        "LocalSpecialEducationStudentID",
        "ReportingSELPA",
        "SpecialEducationInitialEntryStartDate",
        "SpecialEducationStatusEffectiveStartDate",
        "SpecialEducationStatusCode",
        "Non-ParticipationReasonCode",
    ],
    "WBLR": [
        "RecordTypeCode",
        "TransactionTypeCode",
        "LocalRecordID",
        "ReportingLEA",
        "SchoolofAttendance",
        "SchoolofAttendanceNPS",
        "AcademicYearID",
        "SSID",
        "Work-BasedLearningTypeCode",
        "InternshipID",
        "Work-basedLearningHours-External",
        "StateCourseCode-EmbeddedWork-basedLearning",
        "Internship-EmployerPerformanceEvaluationCode",
        "Internship-LEASponsoredIndicator",
        "Internship-CertificatedSupervisorIndicator",
    ],
    "SSID_match": [
        "Submitted_SENR_ReportingLEA",
        "Submitted_SENR_SchoolofAttendance",
        "Selection",
        "Submitted_SENR_LocalID",
        "Submitted_SENR_Student_LegalLastName",
        "Submited_SENR_Student_LegalFirstName",
        "Submitted_SENR_Student_LegalMiddleName",
        "Result_SENR_SSID",
        "Result_SENR_SSIDCreateDate",
        "Result_MatchCategory",
        "Result_MatchPercentageScore",
        "Submitted_SENR_Gender",
        "Submitted_SENR_BirthDate",
        "Submitted_SENR_BirthCountry",
        "Submitted_SENR_BirthState",
        "Submitted_SENR_GradeLevel",
        "Result_SENR_ReportingLEAName",
        "Result_SENR_SchoolofAttendanceName",
        "Result_SENR_ReportingLEACountyDistrictCode",
        "Result_SENR_SchoolofAttendanceSchoolCode",
        "Result_SENR_EnrollmentStartDate",
        "Result_SENR_EnrollmentExitDate",
        "Result_SINF_Student_LegalLastName",
        "Result_SINF_Student_LegalFirstName",
        "Result_SINF_Student_LegalMiddleName",
        "Result_SINF_Student_AliasLastName",
        "Result_SINF_Student_AlieasFirstName",
        "Result_SINF_Gender",
        "Result_SENR_BirthDate" "Result_SELA_ELASCode",
        "Result_SELA_ELASStartDate",
        "Result_SELA_PrimaryLanguage",
        "Result_SINF_ParentGuardian1FirstName",
        "Result_SINF_ParentGuardian1LastName",
        "Result_SINF_ParentGuardian2FirstName",
        "Result_SINF_ParentGuardian2LastName",
        "Result_SINF_ResidentialAddressLine1",
        "Result_SINF_ResidentialAddressLine2",
        "Result_SINF_ResidentialAddressCityName",
        "Result_SINF_ResidentialAddressStateProvinceCode",
        "Result_SINF_ResidentialAddressZipCode",
        "Result_SINF_MailingAddressLine1",
        "Result_SINF_MailingAddressLine2",
        "Result_SINF_MailingAddressCityName",
        "Result_SINF_MailingAddressStateProvince",
        "Result_SINF_MailingAddressZipCode",
        "Result_SENR_GradeLevel",
        "Result_SINF_BirthState",
        "Result_SINF_BirthCity",
        "Result_SINF_StudentInitialUSSchoolEnrollmentDateK-12",
        "Result_SWDS_SWDIndicator",
    ],
}


def get_extract_columns(extract_name: str) -> list:
    return extractColumns.get(extract_name)





abspath = os.path.dirname(__file__)
raw = pd.read_csv(os.path.join(abspath, "ncesdata_C29D2A2A.csv"), encoding="cp437")

def tweak_school_data(df):
    df.columns = df.columns.str.replace(' ','')
    df.columns = df.columns.str.replace('*','')
    df = df.replace("å", None, regex=True)
    df = df.replace("û", None, regex=True)
    return (
        df.assign(StateSchoolID = lambda df_:df_.StateSchoolID.str[-7:],StateDistrictID = lambda df_:df_.StateDistrictID.str[-7:])
            )

df = tweak_school_data(raw)
near = df.query('CountyName == "El Dorado County" | CountyName == "Amador County" | CountyName == "Alpine County" | CountyName == "Sacramento County" | CountyName == "Placer County"').reset_index(drop=True)
near.to_csv('near_counties.csv',index=False)

elDorado = df.query('CountyName == "El Dorado County"').reset_index(drop=True)
elDorado.to_csv('el_dorado.csv',index=False)





if __name__ == "__main__":
##    print(convert_to_NCSE("0961960"))
####    print(get_extract_columns("WBLR"))
    print(elDorado)
