%define svn 6699

%define uim_version     1.4.0
%define chewing_version 0.3.2

Name:		uim-chewing
Summary:	Chinese input plugin for UIM
Version:	0.0.4.1
Release:	%mkrel -c %svn 1
Group:		System/Internationalization
License:	BSD-like
URL:  		http://people.freedesktop.org/~ekato/download/
Source0:	%{name}-r%{svn}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	uim        >= %{uim_version}
Requires:	libchewing >= %{chewing_version}
# (tv) for uim-module-manager:
BuildRequires:	uim
BuildRequires:	libuim-devel     >= %{uim_version}
BuildRequires:	libchewing-devel >= %{chewing_version}
Buildrequires:	librsvg

%description
Chinese input plugin for UIM.


%prep
%setup -qn %{name}

%build
./autogen.sh
%configure2_5x --enable-maintainer-mode
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unnecessary files
rm -f $RPM_BUILD_ROOT%{_libdir}/uim/plugin/*.{a,la}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
uim-module-manager --register chewing

%postun
uim-module-manager --unregister chewing


%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/uim/*.scm
%{_datadir}/uim/pixmaps/chewing.png
%{_libdir}/uim/plugin/libuim*.so
