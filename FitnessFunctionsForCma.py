from __future__ import division
from math import *
import numpy as np
import sys
import sympy as sy


def counted(fn):
    def wrapper(*args, **kwargs):
        wrapper.called+= 1
        return fn(*args, **kwargs)
    wrapper.called= 0
    wrapper.__name__= fn.__name__
    return wrapper


def RMSE(P,X,Y,function,nParam,nb):

  lis=list(nb);
  for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

  ar=np.array(X)
#  print ar

  funce=function
  for i in range(0,nParam):
       funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])",)
 # print funce
  #print "\n"

  for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
  #funSct='['+funce+' for M in X]'
  #print funct
  try:
      #print funce
      #print P
      Yp=len(Y)*[1]

      for i in range(0,len(Y)):
        if i==0 :
            funce=funce.replace("ar[:,","ar["+str(i)+",")
        else :
            funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")
       # print funce
        Yp[i]=eval(funce)
     # print Yp
      #print Y
      Ys=Yp
      #print P
      #print ar
      n=[(i-j) for i,j in zip(Ys,Y)]
      R= sqrt(sum([(i-j)**2 for i,j in zip(Ys,Y)])/len(Ys))
     # print "r= "+str(R)
      return R
  except:
       print "Unexpected error: asdad ", sys.exc_info()[0],sys.exc_info()[1]
       R=1001
       return R

@counted
def ME(P,X,Y,function,nParam,nb):
#    print 'parametri \n'
   # print P

    #print "a intrat in ME"
    lis=list(nb);
    for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

    ar=np.array(X)
  #print ar

    funce=function
    for i in range(0,nParam):
        funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])")


    for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
    try:

            Yp=len(Y)*[1]

            for i in range(0,len(Y)):
#                print funce
                if i==0 :
                    funce=funce.replace("ar[:,","ar["+str(i)+",")
                else :
                    funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")

                Yp[i]=eval(funce)
               # print P
                #print ar[i,:]
               # print Yp[i]
#            print ar
           # print P

#            print '\n'
            #print Yp
            Ys=Yp
            mean=sum(Y) / int(len(Y))
           # mef=(sum([((j-mean)**2) for i,j in zip(Ys,Y)])-sum([(i-j)**2 for i,j in zip(Ys,Y)]))/sum([(j-mean)**2 for i,j in zip(Ys,Y)])
            sum1=sum([(i-j)**2 for i,j in zip(Ys,Y)])
            sum2=sum([(j-mean)**2 for j in Y])
            meff=(sum1)/sum2
            meffFinal=meff
            #print(str(meffFinal))
            return meffFinal
    except:
         print "Unexpected error:aSsd ", sys.exc_info()
         errMEF=3e50
         return errMEF



@counted
def AIC(P,X,Y,function,nParam,nb):
#    print 'parametri \n'
   # print P

    #print "a intrat in AIC"
    lis=list(nb);
    for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

    ar=np.array(X)
  #print ar

    funce=function
    for i in range(0,nParam):
        funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])")


    for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
    try:

            Yp=len(Y)*[1]

            for i in range(0,len(Y)):
#                print funce
                if i==0 :
                    funce=funce.replace("ar[:,","ar["+str(i)+",")
                else :
                    funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")

                Yp[i]=eval(funce)
 #               print P
#                print ar[i,:]
               # print Yp[i]
#            print ar
           # print P

#            print '\n'
#            print Yp
            Ys=Yp#predicted values

            #mean=sum(Y) / int(len(Y))
       #      sum1+=pow((*(predicted+i)-*(actual+i)),2);
            RSS=sum([(i-j)**2 for i,j in zip(Ys,Y)])

           # mef=(sum([((j-mean)**2) for i,j in zip(Ys,Y)])-sum([(i-j)**2 for i,j in zip(Ys,Y)]))/sum([(j-mean)**2 for i,j in zip(Ys,Y)])
           # fitness=sampleSize*log(sum1/sampleSize)+(2*programSize*sampleSize)/(programSize-sampleSize-1);
            sampleSize=len(Y);
           # fitnessValue=sampleSize*log(RSS/sampleSize)+(2*nParam*sampleSize)/(sampleSize-nParam-1);
       #sampleSize*log(sum1)+2*programSize+(2*programSize*(programSize+1))/(sampleSize-programSize-1);
            fitnessValue=0
            if sampleSize-nParam-1 != 0:
               fitnessValue=sampleSize*log(RSS/sampleSize)+(2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam-1)
            else :
                fitnessValue=sampleSize*log(RSS/sampleSize)+(2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam)
            #fitnessValue=sampleSize*log(RSS/sampleSize)+nParam*log(sampleSize);#bic
           # fitnessValue=sampleSize*log(RSS/sampleSize)+(2*sampleSize*nParam)/(sampleSize-nParam-1);
            #print str(fitnessValue)
            return fitnessValue
    except:
         print "Unexpected error:Akaike index ", sys.exc_info()
         errAIC=1e50
         return errAIC



@counted
def AICx(P,X,Y,function,nParam,nb):
#    print 'parametri \n'
   # print P

    print "a intrat in AICx"
    lis=list(nb);
    for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

    ar=np.array(X)
  #print ar

    funce=function
    for i in range(0,nParam):
        funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])")


    for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
    try:

            Yp=len(Y)*[1]

            for i in range(0,len(Y)):
#                print funce
                if i==0 :
                    funce=funce.replace("ar[:,","ar["+str(i)+",")
                else :
                    funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")

                Yp[i]=eval(funce)

            Ys=Yp#predicted values

            mean=sum(Y)/int(len(Y))
           # print str(mean)
            RSS=sum([(i-j)**2 for i,j in zip(Ys,Y)])
            RSSMean=sum([(mean-i)**2 for i in Ys])
          #  print str(RSSMean)
            sampleSize=len(Y);
            fitnessValue=0
            maxNumberOfParams=21*4
            if sampleSize-maxNumberOfParams-1 != 0:
               fitnessValue=sampleSize*log((RSS/RSSMean)/sampleSize)+((2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam-1))/(2*maxNumberOfParams+(2*maxNumberOfParams*(maxNumberOfParams+1))/(sampleSize-maxNumberOfParams-1))
            else :
                fitnessValue=sampleSize*log((RSS/RSSMean)/sampleSize)+((2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam))/(2*maxNumberOfParams+(2*maxNumberOfParams*(maxNumberOfParams+1))/(sampleSize-maxNumberOfParams))
            return fitnessValue
    except:
         print "Unexpected error:Akaike index ", sys.exc_info()
         errAIC=1e50
         return errAIC

@counted
def BFF(P,X,Y,function,nParam,nb):
#    print 'parametri \n'
   # print P

    # print "a intrat in BFF"
    lis=list(nb);
    for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

    ar=np.array(X)
  #print ar

    funce=function
    for i in range(0,nParam):
        funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])")


    for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
    try:

            Yp=len(Y)*[1]

            for i in range(0,len(Y)):
#                print funce
                if i==0 :
                    funce=funce.replace("ar[:,","ar["+str(i)+",")
                else :
                    funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")

                Yp[i]=eval(funce)

            Ys=Yp#predicted values

            mean=sum(Y)/int(len(Y))
            #print str(mean)
            RSS=sum([(i-j)**2 for i,j in zip(Ys,Y)])
            RSSMean=sum([(mean-i)**2 for i in Ys])
            # print str(RSSMean)
            sampleSize=len(Y);
            fitnessValue=0
            paramTerm=0
            maxNumberOfParams=11*2
            # print 'maxNumberOfParams'+str(maxNumberOfParams)+'\n'
            if sampleSize-maxNumberOfParams-1 != 0:
               paramTerm=((2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam-1))/(2*maxNumberOfParams+(2*maxNumberOfParams*(maxNumberOfParams+1))/(sampleSize-maxNumberOfParams-1))
            else :
                paramTerm=((2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam))/(2*maxNumberOfParams+(2*maxNumberOfParams*(maxNumberOfParams+1))/(sampleSize-maxNumberOfParams))
            me=ME(P,X,Y,function,nParam,nb)
            cm=ComplexityMeasures(P,X,Y,function,nParam,nb)

            # print 'me='+str(me)+'\n'
            # print 'paramTerm='+str(paramTerm)+'\n'
            # print 'cm='+str(cm)+'\n'
            fitnessValue=sqrt((me)**2+(paramTerm)**2+(cm)**2)
            # print 'fitnessValue='+str(fitnessValue)+'\n'
            return fitnessValue
    except:
         print "Unexpected error:Akaike index ", sys.exc_info()
         errAIC=1e50
         return errAIC
@counted
def BFFNoSE(P,X,Y,function,nParam,nb):
#    print 'parametri \n'
   # print P

    # print "a intrat in BFF"
    lis=list(nb);
    for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

    ar=np.array(X)
  #print ar

    funce=function
    for i in range(0,nParam):
        funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])")


    for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
    try:

            Yp=len(Y)*[1]

            for i in range(0,len(Y)):
#                print funce
                if i==0 :
                    funce=funce.replace("ar[:,","ar["+str(i)+",")
                else :
                    funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")

                Yp[i]=eval(funce)

            Ys=Yp#predicted values

            mean=sum(Y)/int(len(Y))
            #print str(mean)
            RSS=sum([(i-j)**2 for i,j in zip(Ys,Y)])
            RSSMean=sum([(mean-i)**2 for i in Ys])
            # print str(RSSMean)
            sampleSize=len(Y);
            fitnessValue=0
            paramTerm=0
            maxNumberOfParams=11*2
            # print 'maxNumberOfParams'+str(maxNumberOfParams)+'\n'
            if sampleSize-maxNumberOfParams-1 != 0:
               paramTerm=((2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam-1))/(2*maxNumberOfParams+(2*maxNumberOfParams*(maxNumberOfParams+1))/(sampleSize-maxNumberOfParams-1))
            else :
                paramTerm=((2*nParam)+(2*nParam*(nParam+1))/(sampleSize-nParam))/(2*maxNumberOfParams+(2*maxNumberOfParams*(maxNumberOfParams+1))/(sampleSize-maxNumberOfParams))
            me=ME(P,X,Y,function,nParam,nb)
            cm=ComplexityMeasures(P,X,Y,function,nParam,nb)

            #  print 'me='+str(me)+'\n'
            #  print 'paramTerm='+str(paramTerm)+'\n'
            #  print 'cm='+str(cm)+'\n'
            fitnessValue=sqrt((me)**2+(paramTerm)**2)#+(cm)**2)
            # print 'fitnessValue='+str(fitnessValue)+'\n'
            return fitnessValue
    except:
         print "Unexpected error:Akaike index ", sys.exc_info()
         errAIC=1e50
         return errAIC

@counted
def ComplexityMeasures(P,X,Y,function,nParam,nb):
    has_na=0;
    ndemb=4;#enbed dimension
    lis=list(nb);
    epsilon=1e-10;
    nx=len(Y);
    N= 24;
    for i in range(0,len(nb)):
              lis[i]=sy.symbols(lis[i])
  #print lis

    ar=np.array(X);
  #print ar

    funce=function
    for i in range(0,nParam):
        funce=funce.replace("**P["+str(i)+"]","**int(P["+str(i)+"])")


    for i in range(0,len(nb)):
        funce=funce.replace(str(lis[i]),"ar[:,"+str(i)+"]")
    try:

            Yp=len(Y)*[1]
            Residuals=len(Y)*[0]
            xvec=ndemb*[0]
            ipa= [[0 for x in range(0,ndemb)] for x in range(0,ndemb)]
            ifrec=[0 for x in range(0,N)]
            for i in range(0,len(Y)):
                #print funce
                if i==0 :
                    funce=funce.replace("ar[:,","ar["+str(i)+",")
                else :
                    funce=funce.replace("ar["+str(i-1),"ar["+str(i)+"")

                Yp[i]=eval(funce)

                Residuals[i]=Y[i]-Yp[i]

            for nv in range(0,nx-ndemb+1):
              has_na=0;
              for ixvec in range(0,ndemb):
                if np.isnan(Residuals[nv+ixvec]):
                  has_na=1;
                  break;
                xvec[ixvec]=Residuals[nv+ixvec]
              if has_na==1:
                 continue;
              for i in range(0,ndemb):
                for j in range(0,ndemb):
                  ipa[i][j]=0;
              for ilag in range(1,ndemb):
                 for itime in range(ilag,ndemb):
                    ipa[itime][ilag] = ipa[itime-1][ilag-1];
                    if (xvec[itime] <= xvec[itime - ilag]) or (abs(xvec[itime - ilag] - xvec[itime]) < epsilon):
                       ipa[itime][ilag] = ipa[itime][ilag] + 1;

              nd = ipa[ndemb-1][1];

              for ilag in range(2,ndemb):
                 nd =(ilag+1) * nd + ipa[ndemb-1][ilag];

              ifrec[nd] = ifrec[nd] + 1;


            ODPprobs=[0 for x in range(0,N)];
            sumoODP=0;
            ShanCompl=0;
            ODP=ifrec
            sumoODP=sum(ODP)

            for i in range(0,N):
              ODPprobs[i]=ODP[i]/sumoODP;
              if ODPprobs[i]>1e-30 :
               ShanCompl=ShanCompl+ODPprobs[i]*log(ODPprobs[i]);

            ShanCompl=((-1)*ShanCompl)/log(N);#normalizing
            #print(ShanCompl)
            diffCM=1-ShanCompl;#how far is the current complexity from the complexity of white noise=1
            AkaikeValue=AIC(P,X,Y,function,nParam,nb)
            fitness=(diffCM);
            return fitness

    except:
         print "Unexpected error:Complexity Measures ", sys.exc_info()
         errAIC=1e50
         return errAIC


#
#double FitnessFunction::ShannonComplexity(double *ODP)
#{
#    int ndemb;
#    ndemb=4;
#    int  N= dataSize/ndemb;
#    double ODPprobs[N];
#    double sumoODP=0;
#    double ShanCompl=0;
#
#    for(int i=0; i<N; i++)
#    {
#        sumoODP+=*(ODP+i);
#    }
#
#    for(int i=0; i<N; i++)
#    {
#        ODPprobs[i]=*(ODP+i)/sumoODP;
#
#        if(ODPprobs[i]>1e-30)
#        {
#            ShanCompl=ShanCompl+ODPprobs[i]*log(ODPprobs[i]);
#        }
#        else
#        {
#            ShanCompl=ShanCompl+0;
#        }
#    }
#
#    ShanCompl=((-1)*ShanCompl)/log(N);
#    double diffCM=1-ShanCompl;
#
#    delete ODP;
#    return 0.8*AkaikeIndex() +0.2*diffCM;
#}
#
#

#
#@counted
#def CompMes(P,X,Y,function,nParam,nb):
#    compMes=0;
#
#
#    fitness=0.8*AIC(P,X,Y,function,nParam,nb)+0.2*compMes;
#    return fitness



