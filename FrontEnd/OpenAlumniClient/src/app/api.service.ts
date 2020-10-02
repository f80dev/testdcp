import { Injectable } from '@angular/core';
import {$$, api, showError} from "./tools";
import {timeout} from "rxjs/operators";
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {environment} from "../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  user:any;
  token: string=null;
  token_expires: Date;

  constructor(public http:HttpClient) {
    this.token=localStorage.getItem("token");
  }


  getHttpOptions(){
    let httpOptions:any = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json'
      })
    };
    if(!this.token)this.token=localStorage.getItem("token");
    if(this.token)httpOptions.headers["Authorization"]='Token ' + this.token;
    return httpOptions;
  }



  _get(url,params:string="",_timeoutInSec=60){
    url=api(url,params);
    return this.http.get(url,this.getHttpOptions()).pipe(timeout(_timeoutInSec*1000));
  }

  _post(url,params="",body,_timeoutInSec=60){
    url=api(url,params,true,"");
    $$("Appel de "+url)
    return this.http.post(url,body,this.getHttpOptions()).pipe(timeout(_timeoutInSec*1000));
  }

  _delete(url,params="") {
    url=api(url,params,true,"");
    return this.http.delete(url,this.getHttpOptions()).pipe();
  }

  _put(url,params="",body,_timeoutInSec=60){
    url=api(url,params,true,"");
    return this.http.put(url,body,this.getHttpOptions()).pipe(timeout(_timeoutInSec*1000));
  }

  resend(email: string) {
    return this._get("resend","email="+email);
  }

  refreshToken() {
    this.http.post('/api-token-refresh/', JSON.stringify({token: this.token}), this.getHttpOptions()).subscribe(
      data => {
        this.token=data['token'];
      },
      err => {showError(this,err);}
    );
  }

  logout(){
    $$("Déconnexion de l'utilisateur");
    this.token=null;
    this.token_expires = null;
    localStorage.removeItem("token");
    localStorage.removeItem("email");
  }


  getyaml(url:string="",name:string=""){
    let param="";
    if(url.length>0)param="url="+url;
    if(name.length>0)param="name="+name;
    return this._get("getyaml",param);
  }

  updateData(token) {
    this.token = token;
    // decode the token to read the username and expiration timestamp
    const token_parts = this.token.split(/\./);
    const token_decoded = JSON.parse(window.atob(token_parts[1]));
    this.token_expires = new Date(token_decoded.exp * 1000);
    //this.username = token_decoded.username;
  }



   login(user) {
    this.http.post('/api-token-auth/', JSON.stringify(user), this.getHttpOptions()).subscribe(
      data => {
        this.updateData(data['token']);
      },
      err => {showError(this,err);}
    );
  }



  checkCode(email: string, code: any) {
    //let body="username="+email+"&password="+code;
    let body={"username":email,"password":code};
    return this._post("api-token-auth/","",body);
  }



  deluser(address: HTMLElement) {
    return this._get("deluser");
  }


  getuser(email: string) {
    return this._get("extrausers","search="+email);
  }


  register(body:any) {
    return this._post("users/register","",body);
  }



  setuser(fields:any) {
    //if(fields["acceptSponsor"])fields["acceptSponsor"]="True"; else fields["acceptSponsor"]="False";
    return this._put("extrausers/"+fields.id+"/","",fields);
  }

  hello_world() {
    return this._get("helloworld/");
  }

  getPOW() {
    return this._get("pows/");
  }

  addpow(pow: any) {
    if(pow.url=="http://" || pow.url=="https://"){
      pow.url=null;
      pow.text_url=null;
    }
    return this._post("pows/","",pow);
  }

  addwork(work:any) {
    work.dtEnd=work.dtEnd.split("T")[0];
    work.dtStart=work.dtStart.split("T")[0];
    work.profil=environment.domain_server+"/api/profils/"+work.profil+"/";
    work.pow=environment.domain_server+"/api/pows/"+work.pow+"/";
    return this._post("works/","",work);
  }

  getworks(email: any) {
    return this._get("extraworks","search="+email);
  }

  setprofil(data:any) {
    return this._put("profils/"+data.id+"/","",data);
  }


  send(id: string, _from:string,text: any) {
    return this._post("send_to","profil="+id+"&from="+_from,text);
  }

  gettokenforimagesearchengine() {

  }

  searchImage(result: any, number: number, access_token: any) {

  }

  searchPOW(query: string) {
    return this._get("pows","search="+query);
  }

   getfaqs() {
    return this.http.get(api('getyaml',"name=faqs"));
  }
}
