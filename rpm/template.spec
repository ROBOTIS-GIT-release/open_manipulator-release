Name:           ros-kinetic-open-manipulator
Version:        1.0.0
Release:        0%{?dist}
Summary:        ROS open_manipulator package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/open_manipulator
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-kinetic-open-manipulator-description
Requires:       ros-kinetic-open-manipulator-dynamixel-ctrl
Requires:       ros-kinetic-open-manipulator-moveit
Requires:       ros-kinetic-open-manipulator-position-ctrl
BuildRequires:  ros-kinetic-catkin

%description
ROS-enabled OpenManipulator is a full open robot platform consisting of
OpenSoftware​, OpenHardware and OpenCR(Embedded board)​. The OpenManipulator is
allowed users to control it more easily by linking with the MoveIt! package.
Moreover it has full hardware compatibility with TurtleBot3​. Even if you do not
have a real robot, you can control the robot in the Gazebo simulator​.

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
* Fri Jun 01 2018 Pyo <pyo@robotis.com> - 1.0.0-0
- Autogenerated by Bloom

