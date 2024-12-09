import React from 'react';
import './Form.css'; // Jika memiliki file CSS untuk form

function Form() {
  return (
    <div className="container">
      <h1 className="form">REGISTRASI DONOR DARAH</h1><br />
      <form>
        <label htmlFor="Nama">Nama</label>
        <input type="text" placeholder="Nama Lengkap" name="Nama" />

        <label htmlFor="ttl">Tempat Tanggal Lahir</label>
        <input type="text" placeholder="Bandung, 03 Juli 2005" name="ttl" />

        <label htmlFor="ktp">KTP</label>
        <input type="text" placeholder="Masukan 16 Digit Angka" name="ktp" />

        <label htmlFor="job">Pekerjaan</label>
        <select name="job" id="job" defaultValue="">
          <option disabled value="">--Pilih--</option>
          <option value="wiraswasta">Wiraswasta</option>
          <option value="tni">TNI</option>
          <option value="dokter">Dokter</option>
          <option value="guru">Guru</option>
          <option value="irt">Ibu Rumah Tangga</option>
          <option value="not">Tidak Bekerja</option>
        </select>

        <label htmlFor="gender">Jenis Kelamin</label>
        <select name="gender" id="gender" defaultValue="">
          <option disabled value="">--Pilih--</option>
          <option value="laki-laki">Laki-laki</option>
          <option value="perempuan">Perempuan</option>
        </select>

        <label htmlFor="phone">No WhatsApp / Telepon</label>
        <input type="text" placeholder="08123456789" name="phone" />

        <label htmlFor="bloodType">Golongan Darah</label>
        <select name="bloodType" id="bloodType" defaultValue="">
          <option disabled value="">--Pilih--</option>
          <option value="A">A</option>
          <option value="B">B</option>
          <option value="AB">AB</option>
          <option value="O">O</option>
        </select>

        <label htmlFor="diseaseHistory">Riwayat Penyakit</label>
        <select name="diseaseHistory" id="diseaseHistory" defaultValue="">
          <option disabled value="">--Pilih--</option>
          <option value="kanker">Kanker</option>
          <option value="jantung">Jantung</option>
          <option value="hiv/aids">HIV/AIDS</option>
          <option value="opsional">Tidak Memiliki Riwayat Penyakit</option>
        </select>
        <small className="form-note">
          <strong>Note:</strong> Jika anda tidak memiliki penyakit yang tertera maka pilih opsi kosong.
        </small><br />

        <label htmlFor="donorDate">Tanggal Rencana Donor:</label>
        <input className="date" type="date" name="donorDate" />

        <label htmlFor="address">Alamat</label>
        <textarea className="alamat" id="address" name="address" placeholder="Masukan Alamat Lengkap Anda"></textarea>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
}

export default Form;
