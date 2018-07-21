# -*- coding: utf-8 -*-

"""
Created on Sat Jul 21 12:39:55 2018

@author: vinayak sable
"""

from numpy import *
from math import *
__all__ = ['Just_fun','runif','rbinom','rgeom','rnbinom','rpois','rhyper','rmultin','gendis','rexp','rgamma','rnorm','rcauchy','rlaplace','rweibull'

           ]
def Just_fun():
    """

========================
Random Number Generation
========================

==================== =========================================================
Univariate distributions
==============================================================================
rbinom                Binomial distribution.
rexp                  Exponential distribution.
rgamma                Gamma distribution.
rgeom                 Geometric distribution.
rhyper                Hypergeometric distribution.
rlaplace              Laplace distribution.
rnbinom               Negative binomial distribution.
rnorm                 Normal / Gaussian distribution.
rpois                 Poisson distribution.
runif                 Uniform distribution.
rweibull              Weibull distribution.
gendis                General discrete distribution
==================== =========================================================
==================== =========================================================
Multivariate distributions
==============================================================================
rmultin              Multivariate generalization of the binomial distribution.
==================== =========================================================

"""

    return(None)


    #uniform(a,b)
def runif(size=1,low=0,high=1):
        """
        for random number generation from uniform distibution
        """
        assert low<high,"please check your parameter"
        x=[]
        for i in range(size):
            x.append(low+(high-low)*random.random())
        return(array(x))      
    #binomial distribution
def rbinom(m=1,n=1,p=0.5):
        """
        for random number generation from binomial distibution
        """
        assert p>0 and p<1 and n>0, "please check your trial and probability"
        x=[]
        for i in range(m):
            b=lambda p=0.5 : 1 if runif()<=p else 0
            sum=0
            for j in range(n):
                sum+=b(p)
            x.append(sum)
        return array(x)
    #geometric distribution
def rgeom(m=1,p=0.5):
        """
        for random number generation from geometric distibution
        """
        assert p>0 and p<1, "please check your probability"
        x=[]
        for i in range(m):
            g=int(log(runif())/log(1-p))+1
            x.append(g)
        return(array(x))
    
    #negative binomial distribution
def rnbinom(m=1,s=1,p=0.5):
        """
        for random number generation from negative binomial distibution
        """
        assert p>0 and p<1, "please check your probability"
        x=[]
        for i in range(m):
            s1=0
            for j in range(s):
                r=rgeom(1,p)
                s1=s1+r[0]-1  
            x.append(s1)
        return(array(x))
 
    #poisson distribution 
def rpois(m=1,l=1):
        """
        for random number generation from poisson distibution
        """
        assert l>=0, "please check your parameter "
        x=[]
        for i in range(m):
            p=1
            s=0
            while(p>exp(-l)):
                p=p*runif()
                s=s+1
            x.append(s)
        return(array(x))
        
      
    #hypergeometric
def rhyper(m=1,N=10,M=5,n=5):
        """
        for random number generation from hypergeometric distibution
        """
        assert N>=M and N>=n, "check your parameter"
        x=[]
        for i in range(m):
            s=0
            for j in range(1,n+1):
                k=(M-s)/(N-j+1)
                if(runif()<=k):
                    s=s+1
            x.append(s)
        return(array(x))
    
    #multinomial
def rmultin(m,n,p):
        """
        for random number generation from multinomial distribution
        where p is array of probabilities
        """
        assert sum(p)==1,"please check your probabilities"
        x=zeros((m,len(p)))
        for i in range(m):
            for j in range(n):
                e=runif()
                q=0
                for l in range(len(p)):
                    if q<e and e<(q+p[l]):
                        x[i,l]=x[i,l]+1
                    q=q+p[l]    
        return(x)
    
    #General discrete distribution
def gendis(m,x,p):
        """
        for random number generation from General discrete distribution
        where p is array of probabilities
        x is array of numbers
        """        
        assert sum(p)==1,"please check your probabilities"
        y=[]
        for i in range(m):
            e=runif()
            q=0
            for j in range(len(p)):
                if q<=e and e<(q+p[j]):
                    y.append(x[j])
        return(array(y))
    #############################################################################
    #exponential
def rexp(m=1,l=1):
        """
        for random number generation from exponentional distribution
        
        """
        assert l>=0, "please check your parameter"
        x=[]
        for i in range(m):
            x.append((log(1-runif())/(-l)))
        return(array(x))
    
    #GAMMA(n,theta)
def rgamma(m=1,n=1,l=1):
        """
        for random number generation from gamma distribution
        
        """
        assert l>=0, "please check your parameter"
        x=[]
        for i in range(m):
            s=0
            for j in range(n):
                s=s+expo(1,l)[0]
            x.append(s)
        return(array(x))
    #normal(u,s)
def rnorm(m=1,mu=0,s=1):
        """
        for random number generation from normal distribution
        
        """
        assert s>0, "please check your sigma"
        x=[]
        for i in range(m):
            w=(sqrt((-2)*log(runif())))*sin(2*22/7*runif())
            x.append(mu+s*w)
        return(array(x)) 
        
        
        ################################################################
        #cauchy
def rcauchy(m=1,mu=0,l=1):
        """
        for random number generation from cauchy distribution
        
        """
        assert l>0,"please check your second parameter"
        x=[]
        for i in range(m):
            x.append(mu+l*(tan(22/7*(runif()-0.5))))
        return(array(x))
            
def rlaplace(m=1,mu=0,l=1):
        """
        for random number generation from laplace distribution
        
        """
        assert l>0,"please check your second parameter"
        x=[]
        for i in range(m):
            q=runif()
            if q<0.5:
                x.append(mu+((log(2*q))/l))
            else:
                x.append(mu-((log(2*q))/l))
        return(array(x))
        
        #weibull
    
def rweibull(m=1,a=1,b=1):
        """
        for random number generation from weibull distribution
        
        """
        assert a>0 and b>0,"please check your parametet"
        x=[]
        for i in range(m):
            q=runif(1,0,1)
            x.append(a*(-log(1-q)**b))
        return(array(x))


