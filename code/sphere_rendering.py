import matplotlib.pyplot as plt
import numpy as np
#references
#https://www.fabrizioduroni.it/2017/08/25/how-to-calculate-reflection-vector/
#https://medium.com/@bhardwajtarushi2004/phong-model-2498bae081de
#https://www.tutorialspoint.com/plotting-points-on-the-surface-of-a-sphere-in-python-s-matplotlib
np.random.seed(0)
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
u, v = np.mgrid[0:2 * np.pi:50j, 0:np.pi:50j]
#surface normals
r = 1
x = r * np.cos(u)* np.sin(v)
y = r * np.sin(u) * np.sin(v)
z = r * np.cos(v)
normals = np.array([x, y, z]).reshape(3, x.shape[0]*x.shape[1]).T
#source direction
s = np.random.random((3,))
albedo = 1
#lambertian surface
B_lambertian = albedo * np.dot(normals,s)
B_lambertian = B_lambertian.reshape(x.shape)
#print(B_lambertian.shape)
n = 0
#normalize normals along each axis
normals = np.divide(normals, np.linalg.norm(normals, axis=1)[:, np.newaxis])
#normalize source
s = s/np.linalg.norm(s)
#view direction for Phong Reflection
vw = np.random.random((3,))
#normalize view
vw = vw/np.linalg.norm(vw)
#reflection direction
reflection = (2*np.dot(normals,s)[:,np.newaxis]*normals) - s
#normalize reflection direction
reflection = reflection/np.linalg.norm(reflection)
#Phong reflection
B_Phong =  (np.dot(reflection, vw))**n
B_Phong = B_Phong.reshape(x.shape)
#plot 3D surface, Replace B_Phong with B_Lambertian for perfect lambertian surface
ax.plot_surface(x, y, z, facecolors = plt.cm.Reds(B_Phong), rstride = 1, cstride =1)
plt.show()
