import React from 'react';


const InformasiLayanan = () => {
  return (
    <div className="wrapper">
      <div className="content">
        <div className="container mt-5">
          <div className="row">
            {/* Service Card 1 */}
            <div className="col-md-4">
              <div className="layanan-card">
                <i className="fas fa-tint"></i>
                <p>Stok Darah</p>
                <button className="btn btn-light layanan-btn">Ikon</button>
              </div>
            </div>

            {/* Service Card 2 */}
            <div className="col-md-4">
              <div className="layanan-card">
                <i className="fas fa-calendar-alt"></i>
                <p>Jadwal Donor</p>
                <button className="btn btn-light layanan-btn">Ikon</button>
              </div>
            </div>

            {/* Service Card 3 */}
            <div className="col-md-4">
              <div className="layanan-card">
                <i className="fas fa-map-marker-alt"></i>
                <p>Lokasi Donor</p>
                <button className="btn btn-light layanan-btn">Ikon</button>
              </div>
            </div>
          </div>

          <div className="row mt-4">
            {/* Service Card 4 */}
            <div className="col-md-4">
              <div className="layanan-card">
                <i className="fas fa-donate"></i>
                <p>Petugas Medis</p>
                <button className="btn btn-light layanan-btn">Ikon</button>
              </div>
            </div>

            {/* Service Card 5 */}
            <div className="col-md-4">
              <div className="layanan-card">
                <i className="fas fa-comments"></i>
                <p>Relawan</p>
                <button className="btn btn-light layanan-btn">Ikon</button>
              </div>
            </div>

            {/* Service Card 6 */}
            <div className="col-md-4">
              <div className="layanan-card">
                <i className="fas fa-users"></i>
                <p>Donasi</p>
                <button className="btn btn-light layanan-btn">Ikon</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default InformasiLayanan;
