Name:		gnome-shell-extension-taskbar
Version:	50.1
Release:	1%{?dist}
Summary:	GNOME Shell Extension TaskBar

License:	GPLv3+
URL:		https://extensions.gnome.org/extension/584/taskbar/
Source0:	https://github.com/zpydr/gnome-shell-extension-taskbar/archive/%{version}.tar.gz

BuildArch:	noarch
Requires:	gnome-shell >= 3.10

%description
TaskBar displays icons of running applications on the top panel.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/images/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/cs_CZ/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/de/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/fr/LC_MESSAGES/
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/schemas/
cp README %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp LICENSE %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp *.js %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp metadata.json %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp TaskBar.pot %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp stylesheet.css %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp README.md %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/
cp images/* %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/images/
cp locale/cs_CZ/LC_MESSAGES/* %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/cs_CZ/LC_MESSAGES/
cp locale/de/LC_MESSAGES/* %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/de/LC_MESSAGES/
cp locale/fr/LC_MESSAGES/* %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/fr/LC_MESSAGES/
cp schemas/* %{buildroot}%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/schemas/

%files
%doc %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/README
%license %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/LICENSE
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/README.md
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/TaskBar.pot
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/*.js
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/images/*.png
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/images/*.svg
%lang(cs) %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/cs_CZ/LC_MESSAGES/TaskBar.mo
%lang(cs) %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/cs_CZ/LC_MESSAGES/TaskBar.po
%lang(de) %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/de/LC_MESSAGES/TaskBar.mo
%lang(de) %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/de/LC_MESSAGES/TaskBar.po
%lang(fr) %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/fr/LC_MESSAGES/TaskBar.mo
%lang(fr) %{_datadir}/gnome-shell/extensions/TaskBar@zpydr/locale/fr/LC_MESSAGES/TaskBar.po
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/metadata.json
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/schemas/gschemas.compiled
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/schemas/org.gnome.shell.extensions.TaskBar.gschema.xml
%{_datadir}/gnome-shell/extensions/TaskBar@zpydr/stylesheet.css

%changelog
* Thu Mar 24 2016 zpydr <zpydr@openmailbox.org> 50.1-1
- Initial version of the package
