import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { SearchComponent } from './search/search.component';
import { ServiceWorkerModule } from '@angular/service-worker';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { environment } from '../environments/environment';
import { ImportComponent } from './import/import.component';
import {ApiService} from "./api.service";
import {HttpClientModule} from "@angular/common/http";
import {MatCardModule} from "@angular/material/card";
import {MatFormFieldModule} from "@angular/material/form-field";
import {MatButtonModule} from "@angular/material/button";
import {MatSnackBarModule} from "@angular/material/snack-bar";
import { AdminComponent } from './admin/admin.component';
import {MatInputModule} from "@angular/material/input";
import {MatIconModule} from "@angular/material/icon";
import {FormsModule} from "@angular/forms";
import { AboutComponent } from './about/about.component';
import { FaqsComponent } from './faqs/faqs.component';
import { HourglassComponent } from './hourglass/hourglass.component';
import { TutoComponent } from './tuto/tuto.component';
import { ImageSelectorComponent } from './image-selector/image-selector.component';
import { TransPipe } from './trans.pipe';
import {MatProgressSpinnerModule} from "@angular/material/progress-spinner";
import { SafePipe } from './safe.pipe';
import { ProfilComponent } from './profil/profil.component';
import { PublicComponent } from './public/public.component';
import { FilterPipe } from './filter.pipe';
import { LoginComponent } from './login/login.component';
import { PromptComponent } from './prompt/prompt.component';
import { WorkComponent } from './work/work.component';
import {MAT_DIALOG_DATA, MatDialogModule} from '@angular/material/dialog';
import {
  FacebookLoginProvider,
  GoogleLoginProvider,
  SocialAuthService,
  SocialAuthServiceConfig, SocialLoginModule
} from "angularx-social-login";
import {getAuthServiceConfigs} from "./tools";
import { LoginbarComponent } from './loginbar/loginbar.component';
import { ProfilesComponent } from './profiles/profiles.component';
import { EditComponent } from './edit/edit.component';
import { PowComponent } from './pow/pow.component';
import {MatTableModule} from "@angular/material/table";
import { AddpowComponent } from './addpow/addpow.component';
import {MatSelectModule} from "@angular/material/select";
import {MatDatepickerModule} from "@angular/material/datepicker";
import {MatNativeDateModule} from "@angular/material/core";
import { WorksComponent } from './works/works.component';
import { SplashComponent } from './splash/splash.component';
import {QuillModule} from "ngx-quill";
import { WriteComponent } from './write/write.component';
import {TextFieldModule} from "@angular/cdk/text-field";
import { StatsComponent } from './stats/stats.component';
import {ImageCropperModule} from "ngx-image-cropper";
import {MatGridListModule} from "@angular/material/grid-list";
import {MatSidenavModule} from "@angular/material/sidenav";
import {MatToolbarModule} from "@angular/material/toolbar";
import {MatListModule} from "@angular/material/list";
import {MatCheckboxModule} from "@angular/material/checkbox";
import {MatExpansionModule} from "@angular/material/expansion";
import { PowsComponent } from './pows/pows.component';
import {NgChatModule} from "ng-chat";
import {OverlayModule} from "@angular/cdk/overlay";
import {MatRadioModule} from "@angular/material/radio";
import { DevComponent } from './dev/dev.component';
import { HtmlEditorComponent } from './html-editor/html-editor.component';
import { BlogComponent } from './blog/blog.component';
import {MatChipsModule} from "@angular/material/chips";
import {MatAutocompleteModule} from "@angular/material/autocomplete";

@NgModule({
  declarations: [
    AppComponent,
    SearchComponent,
    ImportComponent,
    AdminComponent,
    AboutComponent,
    FaqsComponent,
    HourglassComponent,
    TutoComponent,
    ImageSelectorComponent,
    TransPipe,
    SafePipe,
    ProfilComponent,
    PublicComponent,
    FilterPipe,
    LoginComponent,
    PromptComponent,
    WorkComponent,
    LoginbarComponent,
    ProfilesComponent,
    EditComponent,
    PowComponent,
    AddpowComponent,
    WorksComponent,
    SplashComponent,
    WriteComponent,
    StatsComponent,
    PowsComponent,
    DevComponent,
    HtmlEditorComponent,
    BlogComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ScrollingModule,
    QuillModule.forRoot({
      modules: {
        syntax:false,
      },
      theme: 'snow',
      format: 'html',
      readOnly: false,
      placeholder: 'votre article ici'
    }),
    BrowserAnimationsModule,
    MatNativeDateModule,
    ServiceWorkerModule.register('ngsw-worker.js', {enabled: environment.production}),
    MatCardModule,
    MatTableModule,
    MatSnackBarModule,
    ImageCropperModule,
    TextFieldModule,
    SocialLoginModule,
    MatFormFieldModule,
    MatInputModule,
    NgChatModule,
    MatDialogModule,
    MatButtonModule,
    MatIconModule,
    FormsModule,
    MatProgressSpinnerModule,
    MatSelectModule,
    MatDatepickerModule,
    MatGridListModule,
    MatSidenavModule,
    MatToolbarModule,
    MatListModule,
    MatCheckboxModule,
    MatExpansionModule,
    OverlayModule,
    MatRadioModule,
    MatChipsModule,
    MatAutocompleteModule,
    QuillModule
  ],
  providers: [
    ApiService,
    TransPipe,
    {
      provide: 'SocialAuthServiceConfig',
      useValue: {
        autoLogin: false,
        providers: [
          {
            id: GoogleLoginProvider.PROVIDER_ID,
            provider: new GoogleLoginProvider('794055474370-qrdn0gb051k774mtetvo7lifcslmlpgg.apps.googleusercontent.com'),
          },
          {
            id: FacebookLoginProvider.PROVIDER_ID,
            provider: new FacebookLoginProvider('1064548794002409'),
          },
        ],
      } as SocialAuthServiceConfig,
    },
    {provide: MAT_DIALOG_DATA, useValue: {hasBackdrop: false}}
  ],
  bootstrap: [AppComponent]
})

export class AppModule {

}
