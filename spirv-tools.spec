# spirv-tools is used by vkd3d, which is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

%define libname %mklibname spirv-tools 0
%define lib32name %mklib32name spirv-tools 0
%define dev32name %mklib32name -d spirv-tools

Name:		spirv-tools
Version:	2020.2
Release:	2
Group:		Development/Tools
Summary:	Tools for working with SPIR-V, a language for running on GPUs
Source0:	https://github.com/KhronosGroup/SPIRV-Tools/archive/v%{version}.tar.gz
Source100:	%{name}.rpmlintrc
License:	Apache 2.0
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	spirv-headers
Requires:	%{libname} = %{EVRD}

%description
Tools for working with SPIR-V, a language for running on GPUs

%package -n %{libname}
Summary:	Libraries needed for spirv-tools
Group:		System/Libraries

%description -n %{libname}
Libraries needed for spirv-tools

%if %{with compat32}
%package -n %{lib32name}
Summary:	Libraries needed for spirv-tools (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
Libraries needed for spirv-tools

%package -n %{dev32name}
Summary:	Development files for 32-bit spirv-tools
Group:		Development/C++ and C
Requires:	%{name} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}

%description -n %{dev32name}
Development files for 32-bit spirv-tools
%endif

%prep
%autosetup -n SPIRV-Tools-%{version} -p1
%if %{with compat32}
%cmake32	\
	-DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
	-DSPIRV_SKIP_TESTS:BOOL=ON \
	-G Ninja
cd ..
%endif

%cmake	\
	-DSPIRV-Headers_SOURCE_DIR=%{_prefix} \
	-DSPIRV_SKIP_TESTS:BOOL=ON \
	-G Ninja

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%ninja_build -C build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%ninja_install -C build

# FIXME those libraries really need a proper soname
%files -n %{libname}
%{_libdir}/*.so

%files
%{_bindir}/*
%{_includedir}/spirv-tools
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/SPIRV-Tools*/*.cmake

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/*.so

%files -n %{dev32name}
%{_prefix}/lib/pkgconfig/*.pc
%{_prefix}/lib/cmake/SPIRV-Tools*
%endif
