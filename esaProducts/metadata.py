# -*- coding: cp1252 -*-
#
# this class encapsulate the metadata info for products 
#
#
import sys
import traceback
from base_metadata import Base_Metadata


METADATA_ACQUISITION_CENTER='METADATA_ACQUISITION_CENTER'
METADATA_ACQUISITION_TYPE='METADATA_ACQUISITION_TYPE'
METADATA_CLOUD_COVERAGE='METADATA_CLOUD_COVERAGE'
METADATA_DATASET_NAME='METADATA_DATASET_NAME'
METADATA_DATA_FILE_PATH='METADATA_DATA_FILE_PATH'
METADATA_DATASET_PRODUCTION_DATE='METADATA_DATASET_PRODUCTION_DATE'
METADATA_FILECLASS='METADATA_FILECLASS'
METADATA_FOOTPRINT='METADATA_FOOTPRINT'
METADATA_FRAME='METADATA_FRAME'
METADATA_GENERATION_TIME='METADATA_GENERATION_TIME'
METADATA_INCIDENCE_ANGLE='METADATA_INCIDENCE_ANGLE'
METADATA_INSTRUMENT='METADATA_INSTRUMENT'
METADATA_INSTRUMENT_ID='METADATA_INSTRUMENT_ID'
METADATA_ORBIT='METADATA_ORBIT'
METADATA_PATH='METADATA_PATH'
METADATA_PLATFORM='METADATA_PLATFORM'
METADATA_PLATFORM_ID='METADATA_PLATFORM_ID'
METADATA_PROCESSING_TIME='METADATA_PROCESSING_TIME'
METADATA_PROCESSING_CENTER='METADATA_PROCESSING_CENTER'
METADATA_PRODUCTNAME='METADATA_PRODUCTNAME'
METADATA_PACKAGENAME='METADATA_PACKAGENAME'
METADATA_PRODUCT_SIZE='METADATA_PRODUCT_SIZE'
METADATA_REFERENCE_SYSTEM_IDENTIFIER='METADATA_REFERENCE_SYSTEM_IDENTIFIER'
METADATA_RESPONSIBLE='METADATA_RESPONSIBLE'
METADATA_REPORT_TYPE='METADATA_REPORT_TYPE'
METADATA_SENSOR_NAME='METADATA_SENSOR_NAME'
METADATA_SENSOR_TYPE='METADATA_SENSOR_TYPE'
METADATA_SENSOR_CODE='METADATA_SENSOR_CODE'
METADATA_SRC_BROWSE_PATH='METADATA_SRC_BROWSE_PATH'
METADATA_SRC_THUMBNAIL_PATH='METADATA_SRC_THUMBNAIL_PATH'
METADATA_START_DATE='METADATA_START_DATE'
METADATA_STOP_DATE='METADATA_STOP_DATE'
METADATA_START_TIME='METADATA_START_TIME'
METADATA_STOP_TIME='METADATA_STOP_TIME'
METADATA_STATUS='METADATA_STATUS'
METADATA_SUN_AZIMUTH='METADATA_SUN_AZIMUTH'
METADATA_SUN_ELEVATION='METADATA_SUN_ELEVATION'
METADATA_TRACK='METADATA_TRACK'
METADATA_TYPECODE='METADATA_TYPECODE'
METADATA_URL='METADATA_URL'
METADATA_VERSION='METADATA_VERSION'
METADATA_VIEWING_ANGLE='METADATA_VIEWING_ANGLE'
METADATA_WRS_LONGITUDE_GRID_NORMALISED='METADATA_WRS_LONGITUDE_GRID_NORMALISED'
METADATA_WRS_LATITUDE_GRID_NORMALISED='METADATA_WRS_LATITUDE_GRID_NORMALISED'




class Metadata(Base_Metadata):
    #counter=0
    #
    
    METADATA_FIELDS=[METADATA_CLOUD_COVERAGE, METADATA_GENERATION_TIME,METADATA_PRODUCTNAME,METADATA_PRODUCT_SIZE,METADATA_PATH,METADATA_START_DATE,METADATA_STOP_DATE,METADATA_START_TIME,METADATA_STOP_TIME,
                 METADATA_TYPECODE,METADATA_PLATFORM,METADATA_PLATFORM_ID,METADATA_FILECLASS,METADATA_FOOTPRINT,METADATA_ORBIT,
                 METADATA_TRACK,METADATA_FRAME,METADATA_VERSION,METADATA_URL,METADATA_PROCESSING_TIME,METADATA_DATASET_NAME,METADATA_SENSOR_NAME,
                 METADATA_SENSOR_CODE,METADATA_DATA_FILE_PATH,METADATA_DATASET_PRODUCTION_DATE,METADATA_INCIDENCE_ANGLE,METADATA_VIEWING_ANGLE,
                 METADATA_SUN_AZIMUTH,METADATA_SUN_ELEVATION,METADATA_REFERENCE_SYSTEM_IDENTIFIER,METADATA_REPORT_TYPE]

    #debug=0
    # the metadata dictionnary
    #dict=None
    # the mapping of nodes used in xml report. keys is node path
    #xmlNodeUsedMapping={}
    
    def __init__(self, defaults=None):
        self.dict={}
        self.counter=0
        for item in self.METADATA_FIELDS:
            self.dict[item] = None
        if defaults!=None:
            for item in defaults.iterkeys():
                self.dict[item] = defaults[item]
        if self.debug!=0:
            print ' init Metadata done'
            

    def eval(self, expr):
        #print "%%%%%%%%%%%%%%%%%%%%%% wil eval:'%s'" % expr
        try:
            if not expr[0:5] == 'self.':
                expr="self.%s" % (expr)
            #print "@@@@@@@@@@@@@@@@  WIL EVAL:'%s'" % expr
            res=eval(expr)
        except:
            xc_type, exc_obj, exc_tb = sys.exc_info()
            res="%s%s%s" % (xc_type, exc_obj, exc_tb)
            traceback.print_exc(file=sys.stdout)
        return res

    def getMetadataNames(self):
        res=[]
        # copy defaults fieds
        for item in self.dict.iterkeys():
            res.append(item)
        # add extra fields
        return res

    def setMetadataPair(self, name=None, value=None):
        self.dict[name] = value

    def getMetadataValue(self,name=None):
        if self.dict.has_key(name):
            return self.dict[name]
        else:
            return "NOT-PRESENT"

    def getNextCounter(self):
        self.counter=self.counter+1
        return self.counter


    
if __name__ == '__main__':
    met=Metadata()
    met.dump()
    met.setMetadataPair('a','aaa')
    print "set a=aaa"
    met.dump()
    print "get a:%s" % met.getMetadataValue('a')
    print "get b:%s" % met.getMetadataValue('b')
