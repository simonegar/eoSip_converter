# -*- coding: cp1252 -*-
#
# this class encapsulate the metadata info for browse 
#
#
import sys
import traceback
from base_metadata import Base_Metadata

BROWSE_METADATA_BROWSE_CHOICE='BROWSE_METADATA_BROWSE_CHOICE'
BROWSE_METADATA_IDENTIFIER='BROWSE_METADATA_IDENTIFIER'
BROWSE_METADATA_FILENAME='BROWSE_METADATA_FILENAME'
BROWSE_METADATA_NAME='BROWSE_METADATA_NAME'
BROWSE_METADATA_REPORT_NAME='BROWSE_METADATA_REPORT_NAME'
BROWSE_METADATA_IMAGE_TYPE='BROWSE_METADATA_IMAGE_TYPE'
#BROWSE_METADATA_REFERENCE_SYSTEM='BROWSE_METADATA_REFERENCE_SYSTEM'
BROWSE_METADATA_START_DATE='BROWSE_METADATA_START_DATE'
BROWSE_METADATA_START_TIME='BROWSE_METADATA_START_TIME'
BROWSE_METADATA_STOP_DATE='BROWSE_METADATA_STOP_DATE'
BROWSE_METADATA_STOP_TIME='BROWSE_METADATA_STOP_TIME'
BROWSE_METADATA_BROWSE_TYPE='BROWSE_METADATA_BROWSE_TYPE'
BROWSE_METADATA_RECT_COORDLIST='BROWSE_METADATA_RECT_COORDLIST'
METADATA_BROWSE_CHOICE='METADATA_BROWSE_CHOICE'


class Browse_Metadata(Base_Metadata):
    #counter=0
    #
    
    METADATA_FIELDS=[BROWSE_METADATA_IDENTIFIER, BROWSE_METADATA_FILENAME, BROWSE_METADATA_IMAGE_TYPE,
                     BROWSE_METADATA_START_DATE, BROWSE_METADATA_START_TIME,
                     BROWSE_METADATA_STOP_DATE, BROWSE_METADATA_STOP_TIME, BROWSE_METADATA_BROWSE_TYPE]

    #
    #debug=0
    #dict={}

    
    def __init__(self, defaults=None):
        self.dict={}
        self.counter=0
        for item in self.METADATA_FIELDS:
            self.dict[item] = None
        if defaults!=None:
            for item in defaults.iterkeys():
                self.dict[item] = defaults[item]
        if self.debug!=0:
            print ' init Browse_Metadata done'


    #def setUsedInXmlMap(self, adict=None):
    #    self.xmlNodeUsedMapping=adict

        
    def eval(self, expr):
        try:
            if not expr[0:5] == 'self.':
                expr="self.%s" % (expr)
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
        self.dict[name]=value


    def getMetadataValue(self,name=None):
        if self.dict.has_key(name):
            return self.dict[name]
        else:
            return "NOT-PRESENT"


    def getNextCounter(self):
        self.counter=self.counter+1
        return self.counter




    
if __name__ == '__main__':
    met=Browse_Metadata()
    met.dump()
    met.setMetadataPair('a','aaa')
    print "set a=aaa"
    met.dump()
    print "get a:%s" % met.getMetadataValue('a')
    print "get b:%s" % met.getMetadataValue('b')
