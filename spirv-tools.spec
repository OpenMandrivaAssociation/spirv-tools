Name:		spirv-tools
Version:	2018.0
Release:	2
Group:		Development/Tools
Summary:	Tools for working with SPIR-V, a language for running on GPUs
Source0:	https://github.com/KhronosGroup/SPIRV-Tools/archive/v%{version}.tar.gz
Source100:	%{name}.rpmlintrc
License:	Apache 2.0
BuildRequires:	cmake ninja
BuildRequires:	spirv-headers

%description
Tools for working with SPIR-V, a language for running on GPUs

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

%files
%{_bindir}/*
%{_includedir}/spirv-tools
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
