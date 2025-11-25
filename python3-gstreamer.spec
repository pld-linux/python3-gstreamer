%define		gst_ver	1.26.0
%define		pname	gst-python
Summary:	GStreamer Python 3 bindings
Summary(pl.UTF-8):	Wiązania języka Python 3 do GStreamera
Name:		python3-gstreamer
Version:	1.26.8
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.xz
# Source0-md5:	5a887d6a086b8eb88767793df5f32197
URL:		https://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	gstreamer-plugins-bad-devel >= %{gst_ver}
BuildRequires:	meson >= 1.4
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python3-devel >= 1:3.7
BuildRequires:	python3-pygobject3-devel >= 3.8
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.042
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

%build
%meson \
	--default-library=shared \
	-Dplugin=enabled \
	-Dpygi-overrides-dir=%{py3_sitedir}/gi/overrides \
	-Dtests=disabled

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}

install -d $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/python

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README.md RELEASE
%attr(755,root,root) %{py3_sitedir}/gi/overrides/_gi_gst.cpython-*.so
%attr(755,root,root) %{py3_sitedir}/gi/overrides/_gi_gst_analytics.cpython-*.so
%{py3_sitedir}/gi/overrides/Gst.py
%{py3_sitedir}/gi/overrides/GstAnalytics.py
%{py3_sitedir}/gi/overrides/GstAudio.py
%{py3_sitedir}/gi/overrides/GstPbutils.py
%{py3_sitedir}/gi/overrides/GstVideo.py
%{py3_sitedir}/gi/overrides/__pycache__/Gst.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstAnalytics.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstAudio.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstPbutils.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstVideo.*.py[co]

%files -n gstreamer-python3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstpython.so
%dir %{_libdir}/gstreamer-1.0/python
