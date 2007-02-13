Summary:	linSerial class - simple, basic framework for managing a serial port
Summary(pl.UTF-8):	Klasa linSerial - prosty, podstawowy szkielet do zarządzania portem szeregowym
Name:		libserial
Version:	0.1.1
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://linas.org/serial/%{name}-%{version}.tar.gz
# Source0-md5:	ca410829859ba722af2c710808b42b82
URL:		http://linas.org/serial/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The linSerial class provides a simple, basic framework for managing a
serial port. The design of this class is focused on making serial port
easy to use, hiding the complexity of the full Linux/Unix termios
interface. The goal is to make writing programs for modems, serial
printers and other serial-attached devices easy for the novice serial
port programmer.

The package includes a flexible error-reporting class.

%description -l pl.UTF-8
Klasa linSerial dostarcza prosty, podstawowy szkielet do zarządzania
portem szeregowym. Projekt tej klasy skupia się na uczynieniu portu
szeregowego łatwym w użyciu i ukryciu złożoności pełnego linuksowego
i uniksowego interfejsu termios. Celem jest ułatwienie początkującym
pisania programów dla modemów, drukarek szeregowych i innych urządzeń
podłączanych w ten sposób.

Pakiet zawiera także elastyczną klasę do raportowania błędów.

%prep
%setup -q -n %{name}-0.1

%build
# Makefile doesn't allow passing necessary options
%{__cxx} %{rpmcflags} -c errlog.C
%{__cxx} %{rpmcflags} -c serial.C
%{__cxx} %{rpmcflags} -c demo.C
ar vru libserial.a errlog.o serial.o
%{__cxx} %{rpmldflags} -o demo demo.o libserial.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/libserial}

install libserial.a $RPM_BUILD_ROOT%{_libdir}
install errlog.h serial.h $RPM_BUILD_ROOT%{_includedir}/libserial

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{_libdir}/libserial.a
%{_includedir}/libserial
