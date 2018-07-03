#
# Conditional build:
%bcond_with	doc		# don't build doc
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	flask-babel
Summary:	Extension to Flask that adds i18n and l10n support to any Flask application with the help of babel, pytz and speaklater
Summary(pl.UTF-8):	Rozszerzenie Flask dodające wsparcie dla i18n i l10n przy użyciu babel, pytz i speklater.
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	0.9
Release:	6
License:	BSD
Group:		Libraries/Python
# https://pypi.python.org/packages/source/F/Flask-Babel/Flask-Babel-0.9.tar.gz
Source0:	https://pypi.python.org/packages/source/F/Flask-Babel/Flask-Babel-%{version}.tar.gz
# Source0-md5:	4762e0392303f464d53cbebedfb87ded
URL:		http://github.com/mitsuhiko/flask-babel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-speaklater
%endif
%if %{with python3}
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
BuildRequires:	python3-speaklater
%endif
Requires:	python-jinja2 >= 2.5
Requires:	python-modules
Requires:	python-speaklater
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adds i18n/l10n support to Flask applications with the help of the
Babel library.

# %description -l pl.UTF-8

%package -n python3-%{module}
Summary:	-
Summary(pl.UTF-8):	-
Group:		Libraries/Python
Requires:	python3-jinja2 >= 2.5
Requires:	python3-modules
Requires:	python3-speaklater

%description -n python3-%{module}
Adds i18n/l10n support to Flask applications with the help of the
Babel library.

# %description -n python3-%{module} -l pl.UTF-8

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

%prep
%setup -q -n Flask-Babel-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd docs
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py_sitescriptdir}/flask_babel
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/Flask_Babel-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE README
%{py3_sitescriptdir}/flask_babel
%{py3_sitescriptdir}/Flask_Babel-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
