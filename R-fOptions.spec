#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-fOptions
Version  : 3042.86
Release  : 39
URL      : https://cran.r-project.org/src/contrib/fOptions_3042.86.tar.gz
Source0  : https://cran.r-project.org/src/contrib/fOptions_3042.86.tar.gz
Summary  : Rmetrics - Pricing and Evaluating Basic Options
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-fOptions-lib = %{version}-%{release}
Requires: R-fBasics
Requires: R-timeDate
Requires: R-timeSeries
BuildRequires : R-fBasics
BuildRequires : R-timeDate
BuildRequires : R-timeSeries
BuildRequires : buildreq-R

%description
valuate basic options. This includes the generalized
	Black-Scholes option, options on futures and options on
	commodity futures.

%package lib
Summary: lib components for the R-fOptions package.
Group: Libraries

%description lib
lib components for the R-fOptions package.


%prep
%setup -q -c -n fOptions
cd %{_builddir}/fOptions

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641019004

%install
export SOURCE_DATE_EPOCH=1641019004
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fOptions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fOptions
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library fOptions
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc fOptions || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/fOptions/COPYRIGHT.html
/usr/lib64/R/library/fOptions/DESCRIPTION
/usr/lib64/R/library/fOptions/INDEX
/usr/lib64/R/library/fOptions/Meta/Rd.rds
/usr/lib64/R/library/fOptions/Meta/features.rds
/usr/lib64/R/library/fOptions/Meta/hsearch.rds
/usr/lib64/R/library/fOptions/Meta/links.rds
/usr/lib64/R/library/fOptions/Meta/nsInfo.rds
/usr/lib64/R/library/fOptions/Meta/package.rds
/usr/lib64/R/library/fOptions/NAMESPACE
/usr/lib64/R/library/fOptions/R/fOptions
/usr/lib64/R/library/fOptions/R/fOptions.rdb
/usr/lib64/R/library/fOptions/R/fOptions.rdx
/usr/lib64/R/library/fOptions/help/AnIndex
/usr/lib64/R/library/fOptions/help/aliases.rds
/usr/lib64/R/library/fOptions/help/fOptions.rdb
/usr/lib64/R/library/fOptions/help/fOptions.rdx
/usr/lib64/R/library/fOptions/help/paths.rds
/usr/lib64/R/library/fOptions/html/00Index.html
/usr/lib64/R/library/fOptions/html/R.css
/usr/lib64/R/library/fOptions/tests/doRUnit.R
/usr/lib64/R/library/fOptions/unitTests/Makefile
/usr/lib64/R/library/fOptions/unitTests/runTests.R
/usr/lib64/R/library/fOptions/unitTests/runit.BasicAmericanOptions.R
/usr/lib64/R/library/fOptions/unitTests/runit.BinomialTreeOptions.R
/usr/lib64/R/library/fOptions/unitTests/runit.HestonNandiGarchFit.R
/usr/lib64/R/library/fOptions/unitTests/runit.HestonnandiGarchOption.R
/usr/lib64/R/library/fOptions/unitTests/runit.LowDiscrepancy.R
/usr/lib64/R/library/fOptions/unitTests/runit.MonteCarloOptions.R
/usr/lib64/R/library/fOptions/unitTests/runit.PlainVanillaOptions.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/fOptions/libs/fOptions.so
/usr/lib64/R/library/fOptions/libs/fOptions.so.avx2
/usr/lib64/R/library/fOptions/libs/fOptions.so.avx512
