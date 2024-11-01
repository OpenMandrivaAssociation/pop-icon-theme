Name:           pop-icon-theme
Version:        3.5.1
Release:        1
Summary:        System76 Pop icon theme for Linux
License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/icon-theme
Source0:        https://github.com/pop-os/icon-theme/archive/v%{version}/icon-theme-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  zstd
BuildArch:      noarch
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme

%description
Pop_Icons use a semi-flat design with raised 3D motifs to help give depth to
icons. Included in the theme are flat symbolic (single-color) icons as well as
full-color stylized icons.

%prep
%autosetup -n icon-theme-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE COPYING
%doc README.md
%{_datadir}/icons/Pop
