%define		gst_ver	1.20.0
%define		pname	gst-python
Summary:	GStreamer Python 3 bindings
Summary(pl.UTF-8):	Wiązania języka Python 3 do GStreamera
Name:		python3-gstreamer
Version:	1.20.2
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.xz
# Source0-md5:	9d3c538fbc7ce459ce7a1c35692f8ed9
Patch0:		%{name}-nosegv.patch
URL:		https://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	meson >= 0.59.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-pygobject3-devel >= 3.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gstreamer >= %{gst_ver}
Requires:	python3-pygobject3 >= 3.8
Obsoletes:	python-gstreamer-devel < 1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python 3 bindings.

%description -l pl.UTF-8
Wiązania języka Python 3 do GStreamera.

%package -n gstreamer-python3
Summary:	GStreamer plugin to load plugins written in Python 3
Summary(pl.UTF-8):	Wtyczka GStreamera do wczytywania wtyczek napisanych w Pythonie 3
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
# gstreamer 1.18+ doesn't support python2 anymore
Obsoletes:	gstreamer-python < 1.18

%description -n gstreamer-python3
GStreamer plugin to load plugins written in Python 3.

%description -n gstreamer-python3 -l pl.UTF-8
Wtyczka GStreamera do wczytywania wtyczek napisanych w Pythonie 3.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%build
%meson build \
	--default-library=shared \
	-Dpygi-overrides-dir=%{py3_sitedir}/gi/overrides

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

install -d $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELEASE TODO
%attr(755,root,root) %{py3_sitedir}/gi/overrides/_gi_gst.cpython-*.so
%{py3_sitedir}/gi/overrides/Gst.py
%{py3_sitedir}/gi/overrides/GstAudio.py
%{py3_sitedir}/gi/overrides/GstPbutils.py
%{py3_sitedir}/gi/overrides/GstVideo.py
%{py3_sitedir}/gi/overrides/__pycache__/Gst.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstAudio.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstPbutils.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstVideo.*.py[co]

%files -n gstreamer-python3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstpython.so
%dir %{_libdir}/gstreamer-1.0/python
