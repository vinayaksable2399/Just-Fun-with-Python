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
from __future__ import division, absolute_import, print_function

depends=['simulation','statss']


__all__ = [
        'runif',
        'rbinom',
        'rgeom',
        'rnbinom',
        'rpois',
        'rhyper',
        'rmultin',
        'gendis',
        'rexp',
        'rgamma',
        'rnorm',
        'rcauchy',
        'rlaplace',
        'rweibull',
        'mode',
        'median',
        'avg',
        'var',
        'cov',
        'corr',
        'ntpm'
           ]
