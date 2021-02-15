%global srcname Adafruit_PureIO

Name:           python-%{srcname}
Version:        1.1.8
Release:        0%{?dist}
Summary:        Pure python access to Linux IO including I2C and SPI

License:        MIT
URL:            https://github.com/adafruit/Adafruit_Python_PureIO
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pure python (i.e. no native extensions) access to Linux IO including I2C and SPI.
Drop in replacement for smbus and spidev modules.

%package -n python3-%{srcname}
Summary:        %{summary}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
Pure python (i.e. no native extensions) access to Linux IO including I2C and SPI.
Drop in replacement for smbus and spidev modules.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%doc CODE_OF_CONDUCT.md README.rst
%license LICENSE
%{python3_sitelib}/Adafruit_*

%changelog
