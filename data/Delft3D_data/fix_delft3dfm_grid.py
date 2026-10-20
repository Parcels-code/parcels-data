import xarray as xr
import uxarray as ux

filename = "delft3d-fm-raw.nc"
ds = xr.open_dataset(filename).load()
ds.close()
attrs = ds["Mesh"].attrs
attrs.pop("edge_face_connectivity")
attrs.update(
    node_dimension="nMesh_node",
    face_dimension="nMesh_face",
    edge_dimension="nMesh_edge",
    max_face_nodes_dimension="nMaxMesh_face_nodes",
)

ds.to_netcdf(filename, mode="w")
del(ds)


ds = xr.open_dataset(filename)
grid = ux.Grid.from_dataset(ds)  # 7271 faces, 7259 nodes, n_max_face_nodes=4
