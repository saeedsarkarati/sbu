def make_Pij(pi, pj):
	pix,piy,piz = pi.x-pj.xc, pi.y-pj.yc, pi.z-pj.zc
	pjx,pjy,pjz = pj.x-pj.xc, pj.y-pj.yc, pj.z-pj.zc
	dx = pix[:,np.newaxis]- pjx[np.newaxis, :] 
	dy = piy[:,np.newaxis]- pjy[np.newaxis, :] 
	dz = piz[:,np.newaxis]- pjz[np.newaxis, :] 
	d = np.sqrt (dx*dx + dy*dy + dz*dz)
	Pij = np.zeros_like (d)
	cond1 = pi.index == pj.index
	cond2 = np.logical_and(pi.index != pj.index, pi.ax == pj.ax)
	cond3 = pi.ax != pj.ax

		
	ddx = dx
	ddy = dy
	ddz = dz
	# ~ if pi.ax == pj.ax:
	if pi.ax == 1:
		ddx = dz
		ddy = dx
		ddz = dy
	elif pi.ax == 2:
		ddx = dy
		ddy = dz
		ddz = dx


	Pij[cond1] = saeed_coplanar(pj.l / pj.n, pj.l / pj.n, ddx[cond1], ddy[cond1]) 
	Pij[cond2] = saeed(pj.l/ pj.n, pj.l / pj.n, ddx[cond2], ddy[cond2], ddz[cond2]) 
	Pij[cond3] = perpendicular(pj.l/ pj.n, pj.l / pj.n, ddx[cond3], ddy[cond3], ddz[cond3]) 
	return Pij




