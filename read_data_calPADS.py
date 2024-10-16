import re
import pandas as pd
import extractColumns
import numpy as np


def readSINF(filename):

    # https://www.cde.ca.gov/ds/sp/cl/systemdocs.asp
    # https://www.cde.ca.gov/ds/sp/cl/documents/cfsv152-20240301.docx
    data = pd.read_csv(
        filename,
        sep="^",
        names=extractColumns.extractColumns["SINF"],
        index_col=False,
        parse_dates=[3, 4, 17, 35, 50, 51],
        dtype={
            "reportingLEA": "str",
            "schoolID": "str",
            "raceCode1": "str",
            "raceCode2": "str",
            "raceCode3": "str",
            "raceCode4": "str",
            "raceCode5": "str",
            "parent1HighestGrade": "str",
            "parent1HighestGrade": "str",
        },
    )
    return data


def readSENR(filename):

    # https://www.cde.ca.gov/ds/sp/cl/systemdocs.asp
    # https://www.cde.ca.gov/ds/sp/cl/documents/cfsv152-20240301.docx
    data = pd.read_csv(
        filename,
        sep="^",
        names=extractColumns.extractColumns["SENR"],
        index_col=False,
        parse_dates=[16, 21, 24],
        dtype={
            "reportingLEA": "str",
            "schoolID": "str",
            "NPSschool": "str",
        },
    )
    return data


def readSBAC(filename):

    # https://www.caaspp-elpac.org/s/docs/CAASPP.student_data_layout.2024.pdf

    recordType = []
    ssid = []
    ln = []
    fn = []
    mn = []
    birthDate = []
    gender = []
    grade = []
    gradeAssess = []
    reportingLEA = []
    districtName = []
    schoolCode = []
    schoolName = []
    charterCode = []
    charterIndicator = []
    SPEDdistrict = []
    testOpportunityID1 = []
    testCompletionDate1 = []
    testCompletionDate2 = []
    compositeClaim1Score = []
    compositeClaim1Performance = []

    with open(filename, "r") as f:
        for line in f:
            recordType.append(line[0:2])
            ssid.append(line[2:12])
            ln.append(line[12:62].strip())
            fn.append(line[62:92].strip())
            mn.append(line[92:122].strip())
            birthDate.append(line[122:132])
            gender.append(line[132:133])
            grade.append(line[138:140])
            gradeAssess.append(line[140:142])
            reportingLEA.append(line[142:149])
            districtName.append(line[156:256].strip())
            schoolCode.append(line[256:270])
            schoolName.append(line[270:370].strip())
            charterCode.append(line[370:374])
            charterIndicator.append(line[374:376])
            SPEDdistrict.append(line[376:383])
            testOpportunityID1.append(line[500:516])
            testCompletionDate1.append(line[1544:1554])
            testCompletionDate2.append(line[1564:1574])
            compositeClaim1Score.append(line[2050:2054])
            compositeClaim1Performance.append(line[2054:2055])

        dictdf = {
            "recordType": recordType,
            "ssid": ssid,
            "lastName": ln,
            "firstName": fn,
            "middleName": mn,
            "birthDate": birthDate,
            "gender": gender,
            "grade": grade,
            "gradeAssess": gradeAssess,
            "reportingLEA": reportingLEA,
            "districtName": districtName,
            "schoolCode": schoolCode,
            "schoolName": schoolName,
            "charterCode": charterCode,
            "charterIndicator": charterIndicator,
            "SPEDdistrict": SPEDdistrict,
            "testOpportunityID1": testOpportunityID1,
            "testCompletionDate1": testCompletionDate1,
            "testCompletionDate2": testCompletionDate2,
            "compositeClaim1Score": compositeClaim1Score,
            "compositeClaim1Performance": compositeClaim1Performance,
        }

        return pd.DataFrame(dictdf)


def readCERS(filename):
    data = pd.read_csv(
        filename,
        index_col=False,
        parse_dates=[8],
        dtype={
            "DistrictId": "str",
            "NcesId": "str",
            "SchoolId": "str",
            "GradeLevelWhenAssessed": "str",
        },
    ).assign(DistrictId=lambda df_: df_.DistrictId.str[0:7])

    return data


def readSCSC(filename):
    data = pd.read_csv(
        filename,
        sep="^",
        names=extractColumns.extractColumns["SCSC"],
        index_col=False,
        dtype={
            "reportingLEA": "str",
            "localCourseID": "str",
        },
    )
    return data


def readSELA(filename):
    data = pd.read_csv(
        filename,
        sep="^",
        names=extractColumns.extractColumns["SELA"],
        index_col=False,
        parse_dates=[9, 13, 15, 16],
        dtype={
            "reportingLEA": "str",
            "localCourseID": "str",
        },
    )
    return data


def readELPAC(filename):
    # https://www.caaspp-elpac.org/s/docs/ELPAC.student-data-layout.2023-24.pdf

    recordType = []
    uniqueID = []
    ssid = []
    localid = []
    ln = []
    fn = []
    mn = []
    tkIndicator = []
    birthDate = []
    birthDateTesting = []
    gender = []
    grade = []
    gradeAssess = []
    reportingLEA = []
    districtName = []
    schoolCode = []
    schoolName = []
    charterCode = []
    charterIndicator = []
    SPEDdistrict = []
    testOpportunityID1 = []

    with open(filename, "r") as f:
        for line in f:
            recordType.append(line[0:2])
            uniqueID.append(line[2:18].strip())
            ssid.append(line[50:60])
            localid.append(line[60:75].strip())
            ln.append(line[90:140].strip())
            fn.append(line[140:170].strip())
            mn.append(line[170:200].strip())
            tkIndicator.append(line[200:203])
            birthDate.append(line[205:215])
            birthDateTesting.append(line[215:225])
            gender.append(line[225:226])
            grade.append(line[226:228])
            gradeAssess.append(line[228:230])
            reportingLEA.append(line[230:237])
            districtName.append(line[244:344].strip())
            schoolCode.append(line[344:358])
            schoolName.append(line[358:458].strip())
            charterCode.append(line[458:462])
            charterIndicator.append(line[462:464])
            SPEDdistrict.append(line[465:471])
            testOpportunityID1.append(line[2052:2068])

        dictdf = {
            "recordType": recordType,
            "uniqueID": uniqueID,
            "ssid": ssid,
            "localid": localid,
            "lastName": ln,
            "firstName": fn,
            "middleName": mn,
            "tkIndicator": tkIndicator,
            "birthDate": birthDate,
            "birthDateTesting": birthDateTesting,
            "gender": gender,
            "grade": grade,
            "gradeAssess": gradeAssess,
            "reportingLEA": reportingLEA,
            "districtName": districtName,
            "schoolCode": schoolCode,
            "schoolName": schoolName,
            "charterCode": charterCode,
            "charterIndicator": charterIndicator,
            "SPEDdistrict": SPEDdistrict,
        }

        return pd.DataFrame(dictdf)


def convertSBAC(filename,output_filename):
    # if an SBAC file is givin in excel format only,
    # can we read it in and convert to the correct fixed width .dat format

    # https://www.caaspp-elpac.org/resources/reporting/ssr-and-reporting-resources
    # https://www.caaspp-elpac.org/s/docs/CAASPP.student_data_layout.2022.pdf
    # https://www.caaspp-elpac.org/s/docs/CAASPP.student_data_layout.2023.pdf
    # https://www.caaspp-elpac.org/s/docs/CAASPP.student_data_layout.2024.pdf

    # Ctrl-a Ctrl-c all text in the pdf and use regex to find the widths
    from SBAC_fixed_widths import widths2022
    widths = list(widths2022.values())
    # print(len(widths))
    # print(np.array(widths).sum())


    def convert_to_fixed_width(df, output_file, column_widths):

        # Prepare the fixed-width formatted lines
        with open(output_file, "w") as f:
            for index, row in df.iterrows():
                fixed_width_line = ""
                i=0
                for col, width in zip(df.columns, column_widths):
                    i+=1
                    # print(f'"{i}:{col}":{width},')
                    # Format each column to the specified width
                    fixed_width_line += str(row[col]).ljust(width)
                f.write(fixed_width_line + "\n")

    df = (
        pd.read_excel(
            filename,
            skiprows=1,
            dtype=str,
        )
        .fillna("")
    )
    # print(df)

    # regex = r"\b(\d{1,4}) \(([A-Z]{2})\) (\d{1,4}) (\d{1,4}) (\d{1,4})\b"
    # regex = r"\(([A-Z]{1,2})\) (\d{1,4}) (\d{1,4}) (\d{1,4})\b"

    # with open('pdf_text.txt','r',encoding='utf-8') as pdf_file:
    #     all_text = pdf_file.read()

    # widths = []
    # matches = re.finditer(regex, all_text, re.MULTILINE)

    # for matchNum, match in enumerate(matches, start=1):
        
    #     print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    #     widths.append(int(match.group().split()[-1]))

        # for groupNum in range(0, len(match.groups())):
        #     groupNum = groupNum + 1
            
        #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

    convert_to_fixed_width(df, output_filename, widths)


if __name__ == "__main__":
    convertSBAC("SBAC_2022_09618790000000.xlsx","SBAC_2122_0961879.dat")
