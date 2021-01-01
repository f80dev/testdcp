import {Component, NgModule} from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {SearchComponent} from "./search/search.component";
import {ImportComponent} from "./import/import.component";
import {AdminComponent} from "./admin/admin.component";
import {PublicComponent} from "./public/public.component";
import {LoginComponent} from "./login/login.component";
import {ProfilesComponent} from "./profiles/profiles.component";
import {EditComponent} from "./edit/edit.component";
import {PowComponent} from "./pow/pow.component";
import {AddpowComponent} from "./addpow/addpow.component";
import {WorksComponent} from "./works/works.component";
import {SplashComponent} from "./splash/splash.component";
import {WriteComponent} from "./write/write.component";
import {StatsComponent} from "./stats/stats.component";
import {FaqsComponent} from "./faqs/faqs.component";
import {AboutComponent} from "./about/about.component";
import {PowsComponent} from "./pows/pows.component";
import {DevComponent} from "./dev/dev.component";

const routes: Routes = [
  { path: 'public', component: PublicComponent},
  { path: 'search', component: SearchComponent},
  { path: 'works', component: WorksComponent},
  { path: 'login', component: LoginComponent},
  { path: 'import', component: ImportComponent},
  { path: 'profils', component: ProfilesComponent},
  { path: 'about', component: AboutComponent},
  { path: 'edit', component: EditComponent},
  { path: 'faqs', component: FaqsComponent},
  { path: 'pow', component: PowComponent},
  { path: 'pows', component: PowsComponent},
  { path: 'addpow', component: AddpowComponent},
  { path: 'admin', component: AdminComponent},
  { path: 'dev', component: DevComponent},
  { path: 'stats', component: StatsComponent},
  { path: 'write', component: WriteComponent},
  { path: '', component: SplashComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
