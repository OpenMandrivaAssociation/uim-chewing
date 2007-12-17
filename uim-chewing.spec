%define version	0.0.2
%define release	%mkrel 3.svn4429.1

%define uim_version     1.4.0
%define chewing_version 0.3.091

Name:		uim-chewing
Summary:	Chinese input plugin for UIM
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	BSD-like
URL:  		http://people.freedesktop.org/~ekato/download/
Source0:	%{name}-%{version}.tar.bz2
Patch1:		uim-chewing-latest-trunk.diff
Requires:		uim        >= %{uim_version}
Requires:		libchewing >= %{chewing_version}
# (tv) for uim-module-manager:
BuildRequires:		uim
BuildRequires:		libuim-devel     >= %{uim_version}
BuildRequires:		libchewing-devel >= %{chewing_version}

%description
Chinese input plugin for UIM.


%prep
%setup -q
%patch1 -p1

%build
%configure2_5x
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
%doc AUTHORS COPYING ChangeLog
%{_datadir}/uim/*.scm
%{_libdir}/uim/plugin/libuim*.so
