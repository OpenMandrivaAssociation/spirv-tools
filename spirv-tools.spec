%define libname %mklibname spirv-tools 0

Name:		spirv-tools
Version:	2019.3
Release:	1
Group:		Development/Tools
Summary:	Tools for working with SPIR-V, a language for running on GPUs
Source0:	https://github.com/KhronosGroup/SPIRV-Tools/archive/v%{version}.tar.gz
Source100:	%{name}.rpmlintrc
License:	Apache 2.0
BuildRequires:	cmake ninja
BuildRequires:	spirv-headers
Requires:	%{libname} = %{EVRD}

%description
Tools for working with SPIR-V, a language for running on GPUs

%package -n %{libname}
Summary:	Libraries needed for spirv-tools
Group:		System/Libraries

%description -n %{libname}
Libraries needed for spirv-tools

%prep
%setup -qn SPIRV-Tools-%{version}
%cmake	\
	-DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
	-DSPIRV_SKIP_TESTS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# FIXME those libraries really need a proper soname
%files -n %{libname}
%{_libdir}/*.so

%files
%{_bindir}/*
%{_includedir}/spirv-tools
%{_libdir}/pkgconfig/*.pc
