Name: mythes-pt
Summary: Portuguese thesaurus
%define upstreamid 20060817
Version: 0.%{upstreamid}
Release: 4.2%{?dist}
Source: http://openthesaurus.caixamagica.pt/download/thes_pt_PT_v2.zip
Group: Applications/Text
URL: http://openthesaurus.caixamagica.pt/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
License: GPLv2+
BuildArch: noarch

%description
Portuguese thesaurus.

%prep
%setup -q -c

%build
for i in README_th_pt_PT_v2.txt; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_pt_PT_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes
pushd $RPM_BUILD_ROOT/%{_datadir}/mythes/
pt_PT_aliases="pt_BR"
for lang in $it_IT_aliases; do
        ln -s th_pt_PR_v2.dat "th_"$lang"_v2.dat"
        ln -s th_pt_PR_v2.idx "th_"$lang"_v2.idx"
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_pt_PT_v2.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Apr 26 2010 Dennis Gregorovic <dgregor@redhat.com> - 0.20060817-4.2
- Rebuilt for RHEL 6
Related: rhbz#566527

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20060817-4.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060817-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolan McNamara <caolanm@redhat.com> - 0.20060817-3
- tidy spec

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20060817-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 02 2009 Caolan McNamara <caolanm@redhat.com> - 0.20060817-1
- initial version
