import re
txt='''
We try to quantitatively capture these characteristics by defining a set of indexes, which can be computed using the mosaic image and the corresponding ground truth:
\begin{itemize}
    \item $\mu_{A_T}$ and $\sigma_{A_T}$, the mean and standard deviation of the tiles area $A_T$, respectively;
    \item $\rho_\text{filler}$, the ratio between the filler area and the overall mosaic are, computed as $\rho_\text{filler}=\frac{\sum_{T \in \mathcal{T} A_T}}{A}$, being $A$ the area of the mosaic;
    \item \todo{does it worth?};
    \item \todo{does it worth?};
    \item $\mu_{C_T}$, the mean of the tiles \emph{color dispersion} $C_T$, being $C_T = \sigma_R+\sigma_G+\sigma_B$, where $\sigma_R$, $\sigma_G$ and $\sigma_B$ are the standard deviation of the red, green and blue channel values of the pixels within the tile $T$.
After applying a method to an image, we compare the segmented image (i.e., the result) against the ground truth and assess the performance according to the following three metrics:
\begin{itemize}
    \item average tile precision $P$
    \item average tile recall $R$
    \item tile count error $C$
\end{itemize}
Let $T$ be a tile on the ground truth $\mathcal{T}$ with area $A_T$.
Let $T'$ be the tile in the segmented image which mostly overlaps $T$ and let $A_{T'}$ be the area of $T$; let $A_{T \cap T'}$ be the overlapping area between $T$ and $T'$.
Let $n$ and $n'$ the number of tiles respectively in the ground truth and in the segmented image.
Metrics are defined as:
\begin{align}
    P &amp;= \frac{1}{n} \sum_{T \in \mathcal{T}} \frac{A_{T \cap T'}}{A_{T'}} \\
    R &amp;= \frac{1}{n} \sum_{T \in \mathcal{T}} \frac{A_{T \cap T'}}{A_T} \\
    C &amp;= \frac{|n-n'|}{n}
\end{align}
We try to quantitatively capture these characteristics by defining a set of indexes, which can be computed using the mosaic image and the corresponding ground truth:
\begin{itemize}
    \item $\mu_{A_T}$ and $\sigma_{A_T}$, the mean and standard deviation of the tiles area $A_T$, respectively;
    \item $\rho_\text{filler}$, the ratio between the filler area and the overall mosaic are, computed as $\rho_\text{filler}=\frac{\sum_{T \in \mathcal{T} A_T}}{A}$, being $A$ the area of the mosaic;
    \item \todo{does it worth?};
    \item \todo{does it worth?};
    \item $\mu_{C_T}$, the mean of the tiles \emph{color dispersion} $C_T$, being $C_T = \sigma_R+\sigma_G+\sigma_B$, where $\sigma_R$, $\sigma_G$ and $\sigma_B$ are the standard deviation of the red, green and blue channel values of the pixels within the tile $T$.
After applying a method to an image, we compare the segmented image (i.e., the result) against the ground truth and assess the performance according to the following three metrics:
\begin{itemize}
    \item average tile precision $P$
    \item average tile recall $R$
    \item tile count error $C$
\end{itemize}
Let $T$ be a tile on the ground truth $\mathcal{T}$ with area $A_T$.
Let $T'$ be the tile in the segmented image which mostly overlaps $T$ and let $A_{T'}$ be the area of $T$; let $A_{T \cap T'}$ be the overlapping area between $T$ and $T'$.
Let $n$ and $n'$ the number of tiles respectively in the ground truth and in the segmented image.
Metrics are defined as:
\begin{align}
    P &amp;= \frac{1}{n} \sum_{T \in \mathcal{T}} \frac{A_{T \cap T'}}{A_{T'}} \\
    R &amp;= \frac{1}{n} \sum_{T \in \mathcal{T}} \frac{A_{T \cap T'}}{A_T} \\
    C &amp;= \frac{|n-n'|}{n}
\end{align}
'''
pattern=re.findall(r'\$[^\$]*\$',txt)
print(pattern)