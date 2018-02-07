Name:           ros-kinetic-multi-jackal-description
Version:        0.0.1
Release:        0%{?dist}
Summary:        ROS multi_jackal_description package

Group:          Development/Libraries
License:        CCBY
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-gazebo-ros
Requires:       ros-kinetic-lms1xx
Requires:       ros-kinetic-pointgrey-camera-description
Requires:       ros-kinetic-pointgrey-camera-driver
Requires:       ros-kinetic-robot-state-publisher
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-xacro
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-gazebo-ros
BuildRequires:  ros-kinetic-lms1xx
BuildRequires:  ros-kinetic-pointgrey-camera-description
BuildRequires:  ros-kinetic-pointgrey-camera-driver
BuildRequires:  ros-kinetic-robot-state-publisher
BuildRequires:  ros-kinetic-roslaunch
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-xacro

%description
Launch Jackal states and get the model

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Feb 07 2018 Nick Sullivan <nick.dave.sullivan@gmail.com> - 0.0.1-0
- Autogenerated by Bloom

