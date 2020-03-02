# Matrix3d
Like matrices but 3d

Example:
<pre>
  [a, b, c]
  [d, e, f]
  [g, h, i]
		[j, k, l]
		[m, n, o]
		[p, q, r]
				[s, t, u]
				[v, w, x]
				[y, z, the front-bottom-right corner]
</pre>					
i-direction is from the "back" to the "front" of the 3x3 grids, starting in the plane beginning with a, ending at the plane beginning with s

j-direction is from the top to the bottom of each grid, starting on the row beginning with a, ending on the row beginning with g

k-direction is from the left to right of each row, starting on the element a, ending on the element c
