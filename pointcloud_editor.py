import streamlit as st
import open3d as o3d
import numpy as np
import pyvista as pv
from pyvista import themes
from streamlit_pyvista import stpyvista

st.set_page_config(layout="wide")
st.title("🟢 Point Cloud Editor")

# --- Load or start a point cloud ---
st.sidebar.header("📥 Load / Start")
pcd_file = st.sidebar.file_uploader("Upload .ply file", type=['ply'])

if pcd_file:
    pcd = o3d.io.read_point_cloud(pcd_file.name)
    points = np.asarray(pcd.points)
else:
    points = np.empty((0, 3))
    pcd = o3d.geometry.PointCloud()

# --- Add new points ---
st.sidebar.header("➕ Add Point")
x = st.sidebar.number_input("X", value=0.0)
y = st.sidebar.number_input("Y", value=0.0)
z = st.sidebar.number_input("Z", value=0.0)

if st.sidebar.button("Add Point"):
    new_point = np.array([[x, y, z]])
    points = np.vstack([points, new_point])
    st.sidebar.success(f"Added point: {new_point.flatten()}")

# --- Update point cloud ---
pcd.points = o3d.utility.Vector3dVector(points)

# --- 3D Visualization using PyVista ---
st.header("🧭 Point Cloud Viewer")
plotter = pv.Plotter(window_size=[800, 600], theme=themes.DocumentTheme())
plotter.add_points(points, color="dodgerblue", point_size=5.0)
plotter.view_isometric()
stpyvista(plotter)

# --- Export ---
st.sidebar.header("💾 Export")
if st.sidebar.button("Download as PLY"):
    o3d.io.write_point_cloud("output.ply", pcd)
    with open("output.ply", "rb") as f:
        st.sidebar.download_button("Download PLY", f, "edited_pointcloud.ply", "application/octet-stream")
