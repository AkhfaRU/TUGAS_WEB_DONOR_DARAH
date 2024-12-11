import React from "react";
import { useNavigate } from "react-router-dom";

const FormPage = () => {
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault(); // Mencegah reload halaman
    navigate("/sukses"); // Mengarahkan ke halaman sukses
  };

  return (
    <div className="container">
      <h1 className="form">REGISTRASI DONOR DARAH</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="Nama">Nama</label>
        <input type="text" placeholder="Nama Lengkap" name="Nama" id="Nama" required />

        <label htmlFor="ttl">Tempat Tanggal Lahir</label>
        <input type="text" placeholder="Bandung, 03 Juli 2005" name="ttl" id="ttl" required />

        <label htmlFor="ktp">KTP</label>
        <input type="text" placeholder="Masukan 16 Digit Angka" name="ktp" id="ktp" pattern="\d{16}" title="Harus 16 digit angka" required />

        <label htmlFor="job">Pekerjaan</label>
        <select name="job" id="job" required>
          <option value="" disabled>
            --Pilih--
          </option>
          <option value="wiraswasta">Wiraswasta</option>
          <option value="tni">TNI</option>
          <option value="dokter">Dokter</option>
          <option value="guru">Guru</option>
          <option value="irt">Ibu Rumah Tangga</option>
          <option value="not">Tidak Bekerja</option>
        </select>

        <label htmlFor="subjek">Jenis Kelamin</label>
        <select name="subjek" id="subjek" required>
          <option value="" disabled>
            --Pilih--
          </option>
          <option value="laki-laki">Laki-laki</option>
          <option value="perempuan">Perempuan</option>
        </select>

        <label htmlFor="no">No WhatsApp / Telepon</label>
        <input type="text" placeholder="08123456789" name="no" id="no" pattern="\d+" title="Harus berupa angka" required />

        <label htmlFor="golongan">Golongan Darah</label>
        <select className="golongan" id="golongan" name="golongan" required>
          <option value="" disabled>
            --Pilih--
          </option>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="AB">AB</option>
          <option value="O">O</option>
        </select>

        <label htmlFor="penyakit">Riwayat Penyakit</label>
        <select className="penyakit" id="penyakit" name="penyakit" required>
          <option value="" disabled>
            --Pilih--
          </option>
          <option value="kanker">Kanker</option>
          <option value="jantung">Jantung</option>
          <option value="hiv/aids">HIV/AIDS</option>
          <option value="opsional">Tidak Memiliki Riwayat Penyakit</option>
        </select>
        <small className="form-note">
          <strong>Note: </strong>Jika Anda tidak memiliki penyakit yang tertera, pilih opsi kosong.
        </small>

        <label htmlFor="tanggal">Tanggal Rencana Donor:</label>
        <input className="date" type="date" id="tanggal" name="tanggal" required />

        <label htmlFor="alamat">Alamat</label>
        <textarea className="alamat" id="alamat" name="alamat" placeholder="Masukan Alamat Lengkap Anda" required></textarea>

        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default FormPage;
